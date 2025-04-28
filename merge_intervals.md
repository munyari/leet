# LRU Cache

Link: https://leetcode.com/problems/merge-intervals/

# Assumptions
- input: each element is a 2-list
- not necessarily sorted
- intervals inclusive of bounds

# Examples
```python
intervals = [[1,2], [2,3]]
merge(intervals) # [[1,3]]

merge([[1,4], [6,8], [4,5]]) # [[1,5], [6, 8]]

merge([[1, 5], [2,3], [18,24]]) # [[1,5], [18,24]]
merge([[2, 3], [2,3], [18,24]]) # [[2,3], [18,24]]
```

# Naive Approach
You can build up a graph using an adjaceny list. The graph is a map, where the
key is an interval and value is a list of each interval that it overlaps with.
The intervals can then be separated into connected components with DFS and a
visited set.

The intervals of each connected component are then merged.

O(n^2) time and space.

# Improved Approach
Sort the intervals by the first element (start). Now, we can build up an output
array. As long as the end of one is less than or equal to the start of the
next, they should be merged. The start of a run to merge is the start of the
first one in that run. The end is the max of all ends in that run.

O(n) runtime, O(n) space (O(1) auxillary)
