class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyStack:

    def __init__(self):
        self.len = 0
        self.cur = ListNode(0)

    def push(self, x: int) -> None:
        self.cur.next = ListNode(x, self.cur)
        self.cur = self.cur.next
        self.len += 1

    def pop(self) -> int:
        cur = self.cur.val
        self.cur = self.cur.prev
        self.len -= 1
        return cur

    def top(self) -> int:
        return self.cur.val

    def empty(self) -> bool:
       return self.len == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()