# Exercise 7

## 1. Time complexity of the given `reverse()` implementation

The given implementation has time complexity **O(n^2)**.

### Step-by-step reasoning
- The loop runs from `self.get_size() - 1` down to `0`, so it executes `n` times.
- In each iteration, it calls `self.get_element_at_pos(i)`.
- Since the list is a **singly linked list with no tail pointer**, accessing an element at position `i` requires traversing from the head.
- Therefore, `get_element_at_pos(i)` takes **O(i)** time in the worst case, and generally **O(n)**.
- So the total work is:

\sum_{i=0}^{n-1} O(i) = O(n^2)


Creating new nodes and updating pointers are constant-time operations, so they do not change the overall complexity.

Therefore, the full complexity is:

O(n^2)


## 2. Optimized implementation

An optimized implementation reverses the list **in-place** by changing the `next` pointers directly.

### Changes made
- Instead of repeatedly calling `get_element_at_pos(i)`, traverse the list only once.
- Keep track of:
  - `prev`
  - `curr`
  - `next_node`
- Reverse each pointer as you move through the list.

### Why this is better
- Each node is visited exactly once.
- Each pointer is updated once.
- No repeated traversal from the head is needed.
- No new nodes need to be created.

So the optimized version runs in:

O(n)

which is much better than the original **O(n^2)** implementation.