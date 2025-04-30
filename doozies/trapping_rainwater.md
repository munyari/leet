# Trapping rainwater

Link: https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=two-pointers

# Assumptions
- all heights are non-negative integers

# Examples
```python
[0,1,0,2,1,0,1,3,2,1,2,1] # 6
```

# Naive Approach
We can iterate over the input list. Consider the question of how much water can
be stored in the current column.
That would be found by finding the left wall and right wall from the current
element, that is the largest element to its left and its right.
(Note that self is included here, if we can't find any walls taller than the
current column we won't be able to put any water in the current column).
This column's contribution to the overall is then (min of left, right walls) -
height of current column.

Code:

```python
    def trap2(self, height: List[int]) -> int:
        vol = 0
        for i in range(0, len(height)-1): # i = 0 height = [0,1,0,2,1,0,1,3,2,1,2,1]
            left_max = 0
            for left in range(i, -1, -1): # left = 0
                left_max = max(left_max, height[left]) # 0

            right_max = 0
            for right in range(i, len(height)):
                right_max = max(right_max, height[right])

            vol += min(left_max, right_max) - height[i]
        return vol
```

O(n\*n) time
O(1) space.

# Improved Approach
Take the approach above and pre-compute cumulative maxes

```python
    def trap2(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        vol = 0
        maxs_l = [0] * len(height)
        maxs_l[0] = height[0]
        for i in range(1, len(height)):
            maxs_l[i] = max(height[i], maxs_l[i-1])
        
        maxs_r = [0] * len(height)
        maxs_r[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            maxs_r[i] = max(height[i], maxs_r[i+1])

        for i in range(0, len(height)-1):
            vol += min(maxs_l[i], maxs_r[i]) - height[i]

        return vol
```

O(n) space
O(n) time


Can be done better, with 2 pointers.
```python
    def trap4(self, height: List[int]) -> int:
        vol = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                vol += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                vol += right_max - height[right]
        return vol
```

O(1) space
O(n) time

Intuition: at any point, left\_max form's left's left wall (same for right and
right\_max). So, if `left_max` is less than `right_max`, the `left_max` is the
limiting wall for left, and we can calculate its contribuiton to volume.
Otherwise, do the same on the right side. We can move our pointers past which
ever item we just processed.
