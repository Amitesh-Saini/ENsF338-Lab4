Question 1:  
Arrays:

Pros:  
Less memory, cache-friendly, random access

Cons:   
Fixed size, insertion/deletion

Linked lists:

Pros:  
insertion/deletion (location known), dynamic size 

Cons:   
Extra memory for pointers, no cache locality

Question 2:  
First, copy the new value into the wanted position. Avoids having to delete and insert.  

Question 3:

Insertion sort:  
Insertion sort is feasible because we can move forward/backward using prev/next pointers. This works well because linked lists support sequential access. 

Merge sort:  
Merge sort works naturally with linked lists, because it can split the list by traversing, and merge the list  by rearranging pointers

Question 4:

| Sort type  | Array complexity  | List complexity  | Difference  |
| :---- | :---- | :---- | :---- |
| Merge  | O(n log n) time, O(n) space | O(n log n) time, O(log n) space | Linked list will use a little less extra space compared to an array  |
| Insertion  | O(n²) time, O(1) space | O(n²) time, O(1) space | Linked list avoids shifting elements  |

