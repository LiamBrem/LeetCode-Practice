# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse 2nd half
        curr = slow
        prev = None
        nxt = curr.next

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #merge 
        p1 = head
        p2 = prev
        p1Next = p1.next
        p2Next = p2.next

        while p2Next:
            p1.next = p2
            p1 = p1Next
            p1Next = p1.next

            p2.next = p1
            p2 = p2Next
            p2Next = p2.next
        