# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        def merge2(h1, h2):
            c1, c2 = h1, h2
            dummyNode = ListNode()
            curr = dummyNode

            while c1 and c2:
                if c1.val < c2.val:
                    curr.next = c1
                    c1 = c1.next
                else:
                    curr.next = c2
                    c2 = c2.next

                curr = curr.next

            if not c1 and c2:
                curr.next = c2
            elif not c2 and c1:
                curr.next = c1

            return dummyNode.next

        while len(lists) > 1:
            newRes = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                newRes.append(merge2(l1, l2))

            lists = newRes

        return lists[0]

                

