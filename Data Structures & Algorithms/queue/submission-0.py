class Deque:
    
    def __init__(self):
        self.map = list()

    def isEmpty(self) -> bool:
        return len(self.map) == 0

    def append(self, value: int) -> None:
        self.map.append(value)

    def appendleft(self, value: int) -> None:
        self.map.insert(0, value)

    def pop(self) -> int:
        if len(self.map) == 0:
            return -1
        return self.map.pop(-1)

    def popleft(self) -> int:
        if len(self.map) == 0:
            return -1
        return self.map.pop(0)
