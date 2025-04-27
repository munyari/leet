# LRU Cache

Link: https://leetcode.com/problems/lru-cache/description/

# Assumptions
- keys and values are integers >= 0
- cache fits in memory
- capacity > 0

# Examples
```python
l = LRUCache(1)
l.get(0) # -1
l.put(0, 0) # -1
l.put(1, 1)
l.get(0) # -1
l.get(1) # 1
l.put(1, 2)
l.get(1) # 2

l = LRUCache(1)
l.put(1, 1)
l.put(2, 2)
l.get(1) # 1
l.put(3, 3)
l.get(2) # -1

```
# Naive Approach
Keep a dict underlying the cache, and a python list of keys in the dict. When a
key is added, it's appended to the list. If it's already in the list, it is
first found in the list, and then moved to the end.

This is O(n) space, O(1) get due to map read, O(n) to update the list.

# Improved Approach
Instead, keep a doubly linked list, where the head is the least recently used
element. When a key is touched (either put or get) it is moved to the end of
the list. When we reach capacity, we remove the head of the list. The list
nodes store the key-value pair.

Overall, O(1) time for put and get in the aveverage case.

# Notes
In this impl, sentinel nodes are really useful to smoothe out the edge cases
for us. We keep dummy's at head and tail, so the true head and tail are at
head.next and tail.prev respectively.
