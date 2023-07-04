# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 예외 처리
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next


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
    solution_node = solution.reverseBetween(singly_linked_list('1->2->3->4->5'), 2, 4)
    while solution_node:
        print(solution_node.val, end=' ')
        solution_node = solution_node.next
