# Add Two Numbers

Link: https://leetcode.com/problems/add-two-numbers/description

# Assumptions
- each node is a digit 0 <= d <= 9
- no leading zeros on either number

# Examples
```python
l1 = ListNode(val=9)
l2 = ListNode(val=9)
addTwoNumbers(l1, l2) # ListNode(val=8, next=ListNode(val=1))

l1 = None
l2 = ListNode(val=7, next=ListNode(val=2))
addTwoNumbers(l1, l2) # l2


l1 = ListNode(val=9, next=ListNode(val=0, next=ListNode(val=1)))
l2 = ListNode(val=9)
addTwoNumbers(l1, l2) # ListNode(val=8, next=ListNode(val=1, next=ListNode(val=1)))

l1 = ListNode(val=9)
l2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))
addTwoNumbers(l1, l2) # ListNode(val=8, next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=1))))
```

# Naive Approach
Convert each list to a number, then add them, and construct a new list from that number. 

O(n) space, O(n) time. Honestly, not bad.

# Improved Approach
we can utilize a single loop.
Track digit sum and carry, and a pointer for each list. Add sum of two and
carry, and create a new node and plop it at the end. Remember to handle the
carry after the loop is over.
O(n) time
O(1) auxillary space
