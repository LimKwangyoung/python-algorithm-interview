import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = collections.deque([(root, 0)])  # (node, level)
        while que:
            node, level = que.popleft()
            if node.left:
                que.append((node.left, level + 1))
            if node.right:
                que.append((node.right, level + 1))

        return level + 1


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
