# LRU Cache

Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Assumptions
- string fits in memory
- all lowercase ascii characters and parens

# Examples
```python
() -> ()
(abc) -> (abc)
(abc -> abc
ab)c -> abc
((a(b)c -> a(b)c
```

# Naive Approach
can check validity in O(n)
can delete every possible set of characters in O(n^n)
Combine these two for O(n^(n+1)) brute force

# Improved Approach
Iterate over input. 
stack of opens and stack of closes.
if an close is seen, pop open stack.
otherwise, put it on close stack.
at end, rremove all indices that remain in our stacks.

O(n) runtime
O(n) auxillary space

# Notes

