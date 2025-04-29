# Merge sorted array

Link: https://leetcode.com/problems/merge-sorted-array/

# Assumptions
- nums1 has length (m+n) with the rest of the length zero'd out
    - NOTE: always pay attention to odd details like this as they often inform the approach.


# Examples
```python
merge([1,2,3,0,0,0], 3, [2,5,6], 3) # first is modified to [1,2,2,3,5,6]
pickIndex([1], 1, [], 0) # [1]
```

# Naive Approach
Copy the first array. Now use two pointers reading from the copy and list2, to write to list1.

O(n) space
O(n+m) runtime.

# Improved Approach
Maintain three pointers. One is at the end of l1 (in the zeros), one at the
"actual" end of l1, and one at the end of l2. Build out the list with the
standard 2 pointer approach but from the back.

O(n+m) runtime
O(1) space
