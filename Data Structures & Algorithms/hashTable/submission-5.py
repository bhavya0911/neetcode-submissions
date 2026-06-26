class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.innercapacity = capacity
        self.size = 0
        self.map = [None] * capacity

    def insert(self, key: int, value: int) -> None:
        if key >= self.capacity:
            self.capacity = key * self.capacity
            temp = self.map
            self.map = [None] * self.capacity
            for i in range(len(temp)):
                self.map[i] = temp[i]
        if self.map[key] == None:
            self.size += 1
            self.resize()
        self.map[key] = value
        return None

    def get(self, key: int) -> int:
        if self.map[key] != None:
            return self.map[key]
        return -1

    def remove(self, key: int) -> bool:
        if key > self.capacity:
            return False
        if self.map[key] != None:
            self.map[key] = None
            self.size -= 1
            return True
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.innercapacity

    def resize(self) -> None:
        if self.size * 2 >= self.innercapacity:
            self.innercapacity *= 2
        return None        
