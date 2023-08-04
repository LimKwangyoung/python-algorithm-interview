# Definition for doubly-linked list.
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularDeque:
    def __init__(self, k: int):
        self.head = self.tail = None
        self.cnt = 0
        self.maxlen = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.cnt == 0:
                self.head = self.tail = ListNode(value)
            else:
                self.head.prev = ListNode(value, next=self.head)
                self.head = self.head.prev
            self.cnt += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.cnt == 0:
                self.head = self.tail = ListNode(value)
            else:
                self.tail.next = ListNode(value, prev=self.tail)
                self.tail = self.tail.next
            self.cnt += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.head = self.head.next
            self.cnt -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.tail = self.tail.prev
            self.cnt -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.head.val
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.maxlen


if __name__ == '__main__':
    obj = MyCircularDeque(3)

    print(obj.insertLast(1))
    print(obj.insertLast(2))
    print(obj.insertFront(3))
    print(obj.insertFront(4))
    print(obj.getRear())
    print(obj.isFull())
    print(obj.deleteLast())
    print(obj.insertFront(4))
    print(obj.getFront())
