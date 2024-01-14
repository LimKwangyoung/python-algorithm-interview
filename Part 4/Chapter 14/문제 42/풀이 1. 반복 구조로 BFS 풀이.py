import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 == 깊이
        return depth


if __name__ == '__main__':
    def binary_tree(node: TreeNode, i: int):
        if 2 * i + 1 < len(nodes) and nodes[2 * i + 1] is not None:
            node.left = TreeNode(nodes[2 * i + 1])
            binary_tree(node.left, 2 * i + 1)
        if 2 * i + 2 < len(nodes) and nodes[2 * i + 2] is not None:
            node.right = TreeNode(nodes[2 * i + 2])
            binary_tree(node.right, 2 * i + 2)

    nodes = [3, 9, 20, None, None, 15, 7]
    if nodes:
        tree = TreeNode(nodes[0])
    else:
        tree = None
    binary_tree(tree, 0)

    solution = Solution()
    print(solution.maxDepth(tree))
