# Kth Largest Element Without Sorting

Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Assumptions
- all numbers are positive
- cannot use sort

# Examples
```python
findKthLargest([1,2,3,4,5,6,7], 4) # 5
findKthLargest([5,3,0,0,1], 3) # 1
```

# Naive Approach
Maintain a buffer of length k. For each element, do k comparisons to find its
place in the buffer, and insert it as necessary.
O(n\*k) time
O(k) additional space

# Improved Approach
Initialize a min heap. Push the values of num onto it. At any point, if the
length exceeds k, do a heap pop. Then return the smallest element in the heap.

O(k) additional space
O(n) time

We can also heapify the input if allowed to mutate, then we'd have
O(n+k\*log n) = O(n) time
O(1) auxillary space
