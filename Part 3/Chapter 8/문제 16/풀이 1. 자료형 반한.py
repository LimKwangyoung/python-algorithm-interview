# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next_node, node.next = node.next, prev
            prev, node = node, next_node

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> list:
        lst: list = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev = None
        for r in result:
            node = ListNode(int(r))
            node.next = prev
            prev = node

        return prev

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))

        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))


if __name__ == '__main__':
    def singly_linked_list(val_str: str):
        if not val_str:
            return None
        val_lst = list(map(int, val_str.split('->')))

        head = ListNode(val_lst[0])
        cur = head
        for i in val_lst[1:]:
            cur.next = ListNode(i)
            cur = cur.next

        return head

    solution = Solution()
    solution_node = solution.addTwoNumbers(singly_linked_list('2->4->3'), singly_linked_list('5->6->4'))
    while solution_node:
        print(solution_node.val, end=' ')
        solution_node = solution_node.next
