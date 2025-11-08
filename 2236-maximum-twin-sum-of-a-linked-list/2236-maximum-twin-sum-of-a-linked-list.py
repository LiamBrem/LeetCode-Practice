# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        maxSum = 0

        for i in range(len(arr) // 2):
            s = arr[i] + arr[-(i + 1)]
            maxSum = max(maxSum, s)

        return maxSum
        