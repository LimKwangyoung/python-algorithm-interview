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
    def singly_linked_list(val_lst: str):
        if not val_lst:
            return None
        val_lst = list(map(int, val_lst.split('->')))

        head_node = ListNode(val_lst[0])
        cur_node = head_node
        for i in val_lst[1:]:
            cur_node.next = ListNode(i)
            cur_node = cur_node.next

        return head_node

    solution = Solution()
    print(solution.isPalindrome(singly_linked_list('')))
    print(solution.isPalindrome(singly_linked_list('1->2->2->1')))
