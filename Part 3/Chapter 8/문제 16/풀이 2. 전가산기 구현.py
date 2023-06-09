# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            total = 0
            # 두 입력값의 합 계산
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(total + carry, 10)
            head.next = ListNode(val)
            head = head.next

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
    solution_node = solution.addTwoNumbers(singly_linked_list('2->4->3'), singly_linked_list('5->6->4'))
    while solution_node:
        print(solution_node.val, end=' ')
        solution_node = solution_node.next
