# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: list = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


if __name__ == '__main__':
    def singly_linked_list(val_lst: str) -> ListNode:
        val_lst = list(map(int, val_lst.split('->')))

        head_node = ListNode(val_lst[0])
        cur_node = head_node
        for i in val_lst[1:]:
            cur_node.next = ListNode(i)
            cur_node = cur_node.next
        return head_node

    solution = Solution()
    print(solution.isPalindrome(singly_linked_list('1->2')))
    print(solution.isPalindrome(singly_linked_list('1->2->2->1')))
