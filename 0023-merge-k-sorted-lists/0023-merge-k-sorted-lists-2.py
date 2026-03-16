# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(head1, head2):
            p1, p2 = head1, head2
            temp = ListNode()
            curr = temp
            while p1 and p2:
                if p1.val < p2.val:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next

                curr = curr.next

            if p1:
                curr.next = p1
            if p2:
                curr.next = p2

            return temp.next

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                if i >= len(lists) - 1:
                    temp.append(lists[i])
                else:
                    temp.append(merge(lists[i], lists[i + 1]))

            lists = temp

        return lists[0]
