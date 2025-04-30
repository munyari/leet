# Valid word abbreviation

Link: https://leetcode.com/problems/valid-word-abbreviation/

# Assumptions
- no leading zeros
- all lowercase and numeric
- no consecutive abbreviated sequences

# Examples
```python
validWordAbbreviation("foo", "f2") == True
validWordAbbreviation("foo", "3") == True
validWordAbbreviation("", "0") == True
validWordAbbreviation("bar", "1a1") == True
validWordAbbreviation("foobar", "foo4") == False
```

# Naive Approach
Expand the abbreviation, placing a sentinel character like "\*" in the place of numbers.
Then take 2 pointers. Asterik always matches, otherwise look for exact match.

Can check length of the expansion first, which will bound the algorithm at O(n) time
O(n) auxillary space.

# Improved Approach
A pair of pointers, one on each string. When we encounter a number, parse it and fast forward the pointer in the other string, then continue comparison.
