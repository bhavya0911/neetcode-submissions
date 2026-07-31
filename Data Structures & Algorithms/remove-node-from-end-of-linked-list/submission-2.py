# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 1
        main = head
        while main and main.next:
            l += 1
            main = main.next
        if l == 1:
            return None
        if l == n:
            return head.next
        idx = l - n
        main = head
        for i in range(idx - 1):
            main = main.next
        if main.next.next:
            main.next = main.next.next
        else:
            main.next = None
        return head