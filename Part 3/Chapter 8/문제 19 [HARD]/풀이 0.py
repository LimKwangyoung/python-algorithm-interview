# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head.next:
            return head
        root = node = ListNode(next=head)

        for _ in range(left - 1):
            node = node.next
        left_prev = node
        left_node = node = node.next

        prev = None
        for _ in range(right - left + 1):
            next_node, node.next = node.next, prev
            node, prev = next_node, node
        left_prev.next, left_node.next = prev, node

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
    solution_node = solution.reverseBetween(singly_linked_list('1->2->3->4->5->6'), 2, 3)
    while solution_node:
        print(solution_node.val, end=' ')
        solution_node = solution_node.next
