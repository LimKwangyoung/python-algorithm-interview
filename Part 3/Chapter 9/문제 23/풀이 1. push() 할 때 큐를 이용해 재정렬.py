import collections


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상탤 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


if __name__ == '__main__':
    obj = MyStack()

    print(obj.push(1))
    print(obj.push(2))
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
