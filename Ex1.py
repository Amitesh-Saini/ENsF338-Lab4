# Ex 1/1 

# It is counter intuitave to implement binary search on list as an array would handle much better
# as in binary search we need to find the middle element with arrays this is easy as it will be O(1) - arr[mid] or 
# the whole binary serach takes O(logn) time but in a list you must transverse through the list from head or tail to the middle which is  
# O(n) time making it far less efficent. 

# Ex 1/2

class IntNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class IntegerLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        new_node = IntNode(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def binary_search(self, num):
        left = 0
        right = self.size - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = self.get(mid)

            if mid_value == num:
                return mid
            elif mid_value < num:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)


class IntegerArray:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def binary_search(self, num):
        left = 0
        right = len(self.data) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.data[mid] == num:
                return mid
            elif self.data[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def __str__(self):
        return str(self.data)
    

    # Ex 1/3

    # For a linked list, binary search ends up being O(n) overall, 
    # because getting to the middle is not instant—you have to walk through nodes.

    
import random
import time
import math
import matplotlib.pyplot as plt


sizes = [1000, 2000, 4000, 8000]
array_times = []
linked_times = []

trials = 200

for n in sizes:
    arr = IntegerArray()
    ll = IntegerLinkedList()

    for i in range(n):
        arr.append(i)
        ll.append(i)

    search_values = [random.randint(0, n - 1) for _ in range(trials)]

    start = time.perf_counter()
    for value in search_values:
        arr.binary_search(value)
    end = time.perf_counter()
    array_avg = (end - start) / trials
    array_times.append(array_avg)

    start = time.perf_counter()
    for value in search_values:
        ll.binary_search(value)
    end = time.perf_counter()
    linked_avg = (end - start) / trials
    linked_times.append(linked_avg)


log_fit = [array_times[0] * (math.log2(n) / math.log2(sizes[0])) for n in sizes]
linear_fit = [linked_times[0] * (n / sizes[0]) for n in sizes]

plt.plot(sizes, array_times, 'o-', label='Array binary search')
plt.plot(sizes, linked_times, 's-', label='Linked list binary search')
plt.plot(sizes, log_fit, '--', label='O(log n) fit for array')
plt.plot(sizes, linear_fit, '--', label='O(n) fit for linked list')

plt.xlabel('Input size n')
plt.ylabel('Average search time (seconds)')
plt.title('Average-case Binary Search Performance')
plt.legend()
plt.grid(True)
plt.show()

print("Sizes:", sizes)
print("Array average times:", array_times)
print("Linked list average times:", linked_times)



 