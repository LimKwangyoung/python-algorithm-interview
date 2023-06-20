# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head


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
    solution_1_node = solution.oddEvenList(singly_linked_list('1->2->3->4->5'))
    solution_2_node = solution.oddEvenList(singly_linked_list('2->1->3->5->6->4->7'))

    while solution_1_node:
        print(solution_1_node.val, end=' ')
        solution_1_node = solution_1_node.next
    print()
    while solution_2_node:
        print(solution_2_node.val, end=' ')
        solution_2_node = solution_2_node.next
