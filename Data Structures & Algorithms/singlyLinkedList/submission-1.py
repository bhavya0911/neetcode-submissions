class ListNode:

    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)
        self.len = 0
    
    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        i = 0
        start = self.head
        while i < index and start.next != None:
            start = start.next
            i += 1
        return start.val
        # if i == index and start != None:
        #     return start.val
        # return -1
            

    def insertHead(self, val: int) -> None:
        start = ListNode(val)
        if self.len != 0:
            start.next = self.head
        self.len += 1
        self.head = start

    def insertTail(self, val: int) -> None:
        tail = ListNode(val)
        if self.len == 0:
            self.head = tail
            self.len += 1
        else:
            start = self.head
            while start.next:
                start = start.next
            start.next = ListNode(val)
            self.len += 1

    def remove(self, index: int) -> bool:
        if index >= self.len:
            return False
        if index == 0:
            self.head = self.head.next
            self.len -= 1
            return True
        start = self.head.next
        prev = self.head
        i = 1
        while i < index:
            start = start.next
            prev = prev.next
            i += 1
        prev.next = start.next
        self.len -= 1
        return True

    def getValues(self) -> List[int]:
        if self.len == 0:
            return []
        result = list()
        start = self.head
        while start.next:
            result.append(start.val)
            start = start.next
        result.append(start.val)
        return result
        
