# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        arr = []
        l = 1
        fast = head
        while fast and fast.next:
            arr.append(fast.val)
            l += 1
            fast = fast.next
        arr.append(fast.val)
        i = 0
        while i <= (l / 2) - 1:
            twin = (l - 1 - i)
            res = max(res, arr[i] + arr[twin])
            i += 1
        return res
        