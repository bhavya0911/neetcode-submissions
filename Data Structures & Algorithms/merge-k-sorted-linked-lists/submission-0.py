# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        iter = head
        for lista in lists:
            curr = lista
            while curr.next != None:
                iter.next = ListNode(curr.val)
                iter = iter.next
                curr = curr.next
            iter.next = ListNode(curr.val)
            iter = iter.next
        
        if head.next == None:
            return None

        main = head = head.next
        
        while head.next:
            cur1 = head.next
            while cur1.next:
                if head.val > cur1.val:
                    temp = cur1.val
                    cur1.val = head.val
                    head.val = temp
                cur1 = cur1.next

            if head.val > cur1.val:
                temp = cur1.val
                cur1.val = head.val
                head.val = temp
            head = head.next
    

        return main
        