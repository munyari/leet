# LRU Cache

Link: https://leetcode.com/problems/number-of-islands/

# Assumptions
- input: each cell is either 0 or 1
- input matrix is rectangular
- at least one row and one column

# Examples
```python
[["0"]] # 0
[["1"]] # 1
[["1", "0"], ["0", "1"]] # 2
```

# Naive Approach
The matrix is like a graph. Build up an adjaceny list representing edges with island nodes.
Iterate over matrix. For each one, add everything its connected to to a visited set.
Count how many times you add things that haven't been visited to the visited set.

O(n^2\*m^2) runtime because for each island member, we visit O(n\*m) elements.
Space: O(n\*m) for both the adjaceny list and the visited set.

# Improved Approach
Assume we can modify in place.
Iterate over the input array. When we find a 1, begin a BFS, that modifies the
array. Any 1 connected to the current island is set to 0.


Count how many times we do this.

Time: O(n \* m)
Space: O(min(n, m))

Intuition for the space:
- consider a 1xm or nx1 grid. How many elements would the queue hold at any given time?
The size of the frontier being explored is bounded by the length of the longest
diagonal in the grid, which min(n, m).

- contrast with a stack, whose worst case space complexity is O(n\*m) (true
  implicitly of a recursive solution too)

For more: https://claude.ai/share/c743990e-f684-45e8-b9cb-67f5bcc6c9fb


# Notes
https://leetcode.com/problems/number-of-islands/editorial/comments/2968286/

