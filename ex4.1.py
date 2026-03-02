# ex4.1.py
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2


# Q1) 
# Let n = len(li)
#
# Best case: O(n)
# - If li[i] > 5 is never true, the inner loop never runs.
# - Only the outer loop runs n times.
#
# Worst case: O(n^2)
# - If li[i] > 5 is always true, then for each i (n times),
#   the inner loop runs n times.
# - Total work ~ n * n = n^2
#
# Average case: O(n^2)
# - If a constant fraction of elements is > 5 (e.g., ~1/2),
#   then inner loop runs ~ (fraction*n) times overall.
# - Still proportional to n^2, so O(n^2).


# Q2) Modified version where best, average, worst are equivalent
# We remove dependence on data values, so the same work always happens.
def processdata_same_cases(li):
    for i in range(len(li)):
        for j in range(len(li)):
            li[i] *= 2

# Now best = average = worst = O(n^2)