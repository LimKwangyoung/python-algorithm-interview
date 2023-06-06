# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []

        node = head
        while node is not None:
            lst.append(node.val)
            node = node.next

        return lst == lst[::-1]


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
    print(solution.isPalindrome(singly_linked_list('1->2')))
    print(solution.isPalindrome(singly_linked_list('1->2->2->1')))
