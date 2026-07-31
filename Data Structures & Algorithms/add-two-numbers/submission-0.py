# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = "", ""
        main = l1
        while main.next:
            s1 = str(main.val) + s1 
            main = main.next
        s1 = str(main.val) + s1
        main = l2
        while main.next:
            s2 = str(main.val) + s2
            main = main.next
        s2 = str(main.val) + s2
        val = str(int(s1) + int(s2))
        res = ListNode(0)
        curr = res
        while val:
            curr.next = ListNode(int(val[-1]))
            val = val[:-1]
            curr = curr.next
        return res.next