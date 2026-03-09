def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2


"""
Q1.
Best-case complexity: O(n)
Worst-case complexity: O(n^2)
Average-case complexity: O(n^2)


- The outer loop always runs n times.
- The inner loop only runs when li[i] > 5.
- Best case: no element is greater than 5, so only the outer loop runs -> O(n)
- Worst case: every element is greater than 5, so for each of the n outer iterations,
  the inner loop also runs n times -> O(n^2)
- Average case: if some non-zero fraction of elements are greater than 5, the inner loop
  still runs often enough that the total work grows proportionally to n^2 -> O(n^2)

Q2.
No, best, average, and worst case are not the same in the original code.

A modified version where best, average, and worst case are all the same is below.
Since the inner loop always runs regardless of data values, the complexity is always O(n^2).
"""


def processdata_same_complexity(li):
    for i in range(len(li)):
        for j in range(len(li)):
            li[i] *= 2
