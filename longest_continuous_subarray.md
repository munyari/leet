# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

# Assumptions
- non-empty subarrays includes subarrays of size 1
- limit >= 0

# Examples
```python
longestSubarray([0,1,0,2,1,0,1,3,2,1,2,1], 1) # 3
longestSubarray([12], 55) # 1
```

# Naive Approach
Iterate over the input list.
Have an inner loop, whose variable is the right extent of the subbarray.
Two further nested loops to find the sums.
Track the longest satisfying the condition.
O(n^4) runtime.
O(1) space.


# Improved Approach
Two by 2 matrix, with i being start of the array, j being end of array.
Main diagonal is 1.
[i,j] is set for j > i if [i, j-1] and abs(nums[k]-nums[j]) < limit for k in (i, j-1)
```
for i in len(input):
    matrix[i][i] = 1

for i in len(input):
    for j in i+1 to len(input):
        is_eligible = True
        for k in range(i+1, j):
            if abs(input[k]-input[j]) > limit:
                is_eligible = False
                break
        if is_eligible:
            matrix[i][j] = 0
```
O(n^2) space
O(n^3) time


Can be done better, with 2 pointers.
```
longest = 1
for i in range(0, len(input)):
    left = i-1, right = i+1
    longest_at_i = 1
    while left >= 0 or right <= len(input):
        if is_valid(input, left, right):
            longest_at_i = max(longest_at_i, right-left)
            left -= 1
            right += 1
        elif is_valid(input, left+1, right):
            longest_at_i = max(longest_at_i, right-left-1)
            right += 1
        elif is_valid(input, left, right-1):
            longest_at_i = max(longest_at_i, right-left-1)
            left -= 1
        else:
            break
    longest = max(longest_at_i, longest)

return longest
```

Wait, what if we stored the max and min of every run in the matrix?
`matrix: tuple[is_valid, min, max][][]`

build that up in O(n^2) time.
[i, j] for j > i is valid if [i, j-1] is valid and `abs(nums[i][j]-nums[i][j-1].max) < limt and abs(nums[i][j]-nums[i][j-1].min) < limit`
        

Okay, so that's O(n^2) space.
Okay, so that's O(n^2) to build up the matrix.

Of course there's a 2 pointer way which is even better :)

```
left and right are the bounds of the window.
We create a max heap and a min heap.
while right < n:
  push val and index onto max and min heaps
  while the window is not valid (max-min > limit)
    left = min(max_idx, min_idx) + 1
    while max_heap[0].idx < left:
        max_heap.pop()
    while min_heap[0].idx < right:
        min_heap.pop()

  longest = max(longest, right-left+1)
```

Uses 2 heaps.
O(n log n) runtime, O(n) space.
