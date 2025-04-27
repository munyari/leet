# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        curr_l1 = l1
        curr_l2 = l2
        carry = 0
        dummy = ListNode(0)
        curr_node = dummy
        while curr_l1 or curr_l2:
            node_sum = carry
            if curr_l1:
                node_sum += curr_l1.val
                curr_l1 = curr_l1.next
            if curr_l2:
                node_sum += curr_l2.val
                curr_l2 = curr_l2.next
            digit = node_sum % 10
            carry = 1 if node_sum > 9 else 0
            new_node = ListNode(digit)
            curr_node.next = new_node
            curr_node = curr_node.next
        if carry > 0:
            curr_node.next = ListNode(carry)
        return dummy.next


