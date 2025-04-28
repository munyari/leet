# LRU Cache

Link: https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Assumptions
- all nodes have a value


# Examples
```python
[1] # [[1]]
[1,2,3] # [[2],[1],[3]]
[1,2,None] # [2,1]
[1,None,3] # [1,3]
[1,2,4,3,None,None,None] # [3,2,1,4]
[1,2,4,None,3,None,None] # [2,1,3,4]
[1,2,3,None,None,4,None] # [2,1,4,3]
[1,2,3,None,None,None,4] # [2,1,3,4]
```

# Naive Approach
Can't think of one TBH

# Improved Approach
Create a queue. On to it, we push tuples of depth, column offset from root, and
node. We can keep a variable to track min\_offset.
Loop over q
We push head's left and right onto queue, with depth offset +1, col offset -1 for left, +1 for right.
In a map, have a defaultdict(list) for which we append to map[col\_offset]

later, we'll iterate over our map by columns, and add them to the result.

O(N) time complexity where N is number of nodes in tree.
O(N) space complexity.

# Notes

