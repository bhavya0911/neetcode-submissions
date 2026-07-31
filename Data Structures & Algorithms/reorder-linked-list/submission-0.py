# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        newer = ListNode()
        l = 0

        while head:
            if l % 2 == 0:
                newer.next = head
                newer = newer.next
                head = head.next
            else:
                newer.next = prev
                newer = newer.next
                if prev.next:
                    prev = prev.next
                else:
                    break
            l += 1
        head = newer.next