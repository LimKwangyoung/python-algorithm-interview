# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        node = head

        round_up = 0
        while l1 and l2:
            num = l1.val + l2.val + round_up
            round_up = num // 10
            num %= 10

            l1, l2 = l1.next, l2.next
            node.next = ListNode(num)
            node = node.next

        while l1:
            num = l1.val + round_up
            round_up = num // 10
            num %= 10

            l1 = l1.next
            node.next = ListNode(num)
            node = node.next

        while l2:
            num = l2.val + round_up
            round_up = num // 10
            num %= 10

            l2 = l2.next
            node.next = ListNode(num)
            node = node.next

        if round_up:
            node.next = ListNode(round_up)

        return head.next


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
