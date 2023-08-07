# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        root = node = ListNode()

        while True:
            min_idx, min_val = 0, None

            for i in range(len(lists)):
                if lists[i] is not None and (min_val is None or lists[i].val < min_val):
                    min_idx, min_val = i, lists[i].val

            if min_val is None:
                return root.next
            node.next = lists[min_idx]
            node = node.next
            lists[min_idx] = lists[min_idx].next


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
    solution_node = solution.mergeKLists([
        singly_linked_list('1->4->5'),
        singly_linked_list('1->3->4'),
        singly_linked_list('2->6'),
    ])

    while solution_node:
        print(solution_node.val, end=' ')
        solution_node = solution_node.next
