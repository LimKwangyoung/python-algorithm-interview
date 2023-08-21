# Definition for singly-linked list.
class ListNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.hash_table = [None] * 1000

    def put(self, key: int, value: int) -> None:
        idx = key % 1000
        node = self.hash_table[idx]
        if node:
            while node:
                if node.key == key:
                    node.value = value
                    return
                if node.next is None:
                    node.next = ListNode(key, value)
                node = node.next
        else:
            self.hash_table[idx] = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % 1000
        node = self.hash_table[idx]
        if node:
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % 1000
        node = self.hash_table[idx]
        if node:
            if node.key == key:
                self.hash_table[idx] = node.next
                return
            while node.next:
                if node.next.key == key:
                    node.next = node.next.next
                    return
                node = node.next


if __name__ == '__main__':
    obj = MyHashMap()

    print(obj.put(1, 1))
    print(obj.put(2, 2))
    print(obj.get(1))
    print(obj.get(3))
    print(obj.put(2, 1))
    print(obj.get(2))
    print(obj.remove(2))
    print(obj.get(2))
