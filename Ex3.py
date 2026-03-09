#Ex 3/1 
# The file uses an overallocation strategy. When the array becomes full, 
# it reallocates to a capacity slightly larger than the required 
# size instead of increasing by one element. In list_resize, 
# the new size is computed with newsize + (newsize >> 3) + 6, then rounded, 
# so for large arrays the capacity grows by about 1/8 extra, giving an approximate growth factor of 
# 9/8 = 1.125. This helps make repeated appends efficient. 

#Ex 3/2

import sys

lst = []


empty_size = sys.getsizeof([])
pointer_size = 8

old_capacity = (sys.getsizeof(lst) - empty_size) // pointer_size

for i in range(64):
    lst.append(i)

    current_capacity = (sys.getsizeof(lst) - empty_size) // pointer_size

    if current_capacity != old_capacity:
        print(f"After appending {i}: length = {len(lst)}, capacity changed from {old_capacity} to {current_capacity}")
        old_capacity = current_capacity

# Ex/3/4/5

import time
import matplotlib.pyplot as plt

S = 64
trials = 1000

times_resize = []    # from S to S+1, so 64 -> 65, causes resize
times_noresize = []  # from S-1 to S, so 63 -> 64, no resize

# Measure append from 64 to 65
for _ in range(trials):
    lst = list(range(S))   # length 64, already full
    start = time.perf_counter_ns()
    lst.append(S)
    end = time.perf_counter_ns()
    times_resize.append(end - start)

# Measure append from 63 to 64
for _ in range(trials):
    lst = list(range(S - 1))   # length 63, capacity already enough for 64
    start = time.perf_counter_ns()
    lst.append(S - 1)
    end = time.perf_counter_ns()
    times_noresize.append(end - start)

print("Average time for 64 -> 65 (resize):", sum(times_resize) / trials, "ns")
print("Average time for 63 -> 64 (no resize):", sum(times_noresize) / trials, "ns")

plt.hist(times_resize, bins=30, alpha=0.6, label='64 -> 65 (resize)')
plt.hist(times_noresize, bins=30, alpha=0.6, label='63 -> 64 (no resize)')

plt.xlabel("Append time (ns)")
plt.ylabel("Frequency")
plt.title("Distribution of append times")
plt.legend()
plt.grid(True)
plt.show()

#The two distributions should show that appending from 64 to 65 is 
# usually slower than appending from 63 to 64. The reason is that going 
# from 64 to 65 forces Python to grow the underlying array, which means 
# allocating more memory and copying references to the new storage. 
# In contrast, going from 63 to 64 usually uses already allocated space, so it is just a 
# normal append and is faster.