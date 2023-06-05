# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


if __name__ == '__main__':
    def singly_linked_list(val_str: str):
        if not val_str:
            return None
        val_lst = list(map(int, val_str.split('->')))

        head_node = ListNode(val_lst[0])
        cur_node = head_node
        for i in val_lst[1:]:
            cur_node.next = ListNode(i)
            cur_node = cur_node.next

        return head_node

    solution = Solution()
    print(solution.isPalindrome(singly_linked_list('1->2')))
    print(solution.isPalindrome(singly_linked_list('1->2->2->1')))
