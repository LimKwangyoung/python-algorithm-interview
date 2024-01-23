# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0

            result[0] = max(result[0], left + right)

            return 1 + max(left, right)

        result = [0]
        dfs(root)
        return result[0]
