# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None
            
        if (head.next == None):
            return ListNode(head.val)

        newer = self.reverseList(head.next)
        ans = newer
        while newer.next != None:
            newer = newer.next
        newer.next = ListNode(head.val)
        return ans

                