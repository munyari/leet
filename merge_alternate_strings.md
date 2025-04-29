# Merge alternate strings

Link: https://leetcode.com/problems/merge-strings-alternately/

# Assumptions
- lower case ascii characters

# Examples
```python
mergeAlternately("foo", "bar") == "fboaor"
mergeAlternately("", "bar") == "bar"
mergeAlternately("bar", "") == "bar"
mergeAlternately("foo", "barbaz") == "fboaorbaz"
```

# Naive Approach
N/A

# Improved Approach
Iterate over the shorter of the two strings, put all indices in a list. Any left over from the longer should also be appended.
Finally, join

O(n+m) runtime
O(n+m) space for the new string
