# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        root = prev = ListNode(next=node)
        while node and node.next:
            prev.next, node.next = node.next, node.next.next
            prev.next.next = node

            prev = prev.next.next
            node = prev.next

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
    solution_node = solution.swapPairs(singly_linked_list('1->2->3->4'))
    while solution_node:
        print(solution_node.val, end=' ')
        solution_node = solution_node.next
