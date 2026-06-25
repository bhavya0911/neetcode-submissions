# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = head = None
        while list1 and list2:
            curr = ListNode()
            if list1.val > list2.val:
                curr.val = list2.val
                list2 = list2.next
            else:
                curr.val = list1.val
                list1 = list1.next
                
            if head == None:
                result = curr
                head = curr
            else:
                head.next = curr
                head = curr
        while list1:
            curr = ListNode(list1.val)
            list1 = list1.next

            if head == None:
                result = curr
                head = curr
            else:
                head.next = curr
                head = curr

        while list2:
            curr = ListNode(list2.val)
            list2 = list2.next

            if head == None:
                result = curr
                head = curr
            else:
                head.next = curr
                head = curr
        
        return result
