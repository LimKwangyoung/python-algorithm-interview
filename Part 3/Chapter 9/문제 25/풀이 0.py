class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * (k + 1)
        self.n = k + 1
        self.head = 0
        self.tail = 1

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.n
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = (self.head + 1) % self.n
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.head + 1) % self.n]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.tail - 1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return (self.head + 1) % self.n == self.tail

    def isFull(self) -> bool:
        return self.head == self.tail


if __name__ == '__main__':
    obj = MyCircularQueue(5)

    print(obj.enQueue(10))
    print(obj.enQueue(20))
    print(obj.enQueue(30))
    print(obj.enQueue(40))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.deQueue())
    print(obj.enQueue(50))
    print(obj.enQueue(60))
    print(obj.Rear())
    print(obj.Front())
