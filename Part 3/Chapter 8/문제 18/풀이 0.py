# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        def skip_node(node: ListNode, i: int) -> tuple:
            while i != 1 and node.next:
                node = node.next
                i -= 1
            return node, node.next

        prev = head
        num = 1
        while prev and prev.next:
            node_1 = prev.next
            last_node, node_2 = skip_node(node_1, num)
            if not node_2:
                return head

            last_node.next = node_2.next
            prev.next = node_2
            node_2.next = node_1

            prev = prev.next
            num += 1

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
