class ListNode:

    def __init__(self, val, prev=None):
        self.val = val
        self.prev = prev


class MyStack:

    def __init__(self):
        self.cur = ListNode(0)
        self.org = self.cur

    def push(self, x: int) -> None:
        self.cur = ListNode(x, self.cur)

    def pop(self) -> int:
        cur = self.cur.val
        self.cur = self.cur.prev
        return cur

    def top(self) -> int:
        return self.cur.val

    def empty(self) -> bool:
       return self.org == self.cur
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()