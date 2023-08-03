class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue = [x] + self.queue

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue


if __name__ == '__main__':
    obj = MyQueue()

    print(obj.push(1))
    print(obj.push(2))
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
