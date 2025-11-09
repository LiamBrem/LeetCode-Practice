# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        start = prev

        res = 0 
        while start:
            res = max(head.val + start.val, res)

            start = start.next
            head = head.next

        return res
