class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None] * self.capacity

    def get(self, i: int) -> int:
        return self.map[i]

    def set(self, i: int, n: int) -> None:
        self.map[i] = n

    def pushback(self, n: int) -> None:
        i = self.size
        if self.size == self.capacity:
            self.resize()
        self.map[i] = n
        self.size += 1

    def popback(self) -> int:
        n = self.map[self.size - 1]
        self.size -= 1
        return n

    def resize(self) -> None:
        self.capacity *= 2
        temp = self.map
        self.map = [None] * self.capacity
        for i in range(len(temp)):
            self.map[i] = temp[i]

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity