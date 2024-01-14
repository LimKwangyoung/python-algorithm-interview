import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def maximum_depth(node: TreeNode) -> int:
            depth = 0
            que = collections.deque([node])
            while que:
                depth += 1
                for _ in range(len(que)):
                    node = que.popleft()
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            return depth

        if not root:
            return 0

        result = 0
        if root.left:
            result += maximum_depth(root.left)
            print(result)
        if root.right:
            result += maximum_depth(root.right)

        return result


if __name__ == '__main__':
    def binary_tree(node: TreeNode, i: int):
        if 2 * i + 1 < len(nodes) and nodes[2 * i + 1] is not None:
            node.left = TreeNode(nodes[2 * i + 1])
            binary_tree(node.left, 2 * i + 1)
        if 2 * i + 2 < len(nodes) and nodes[2 * i + 2] is not None:
            node.right = TreeNode(nodes[2 * i + 2])
            binary_tree(node.right, 2 * i + 2)

    nodes = [1, 2, 3, 4, 5]
    if nodes:
        tree = TreeNode(nodes[0])
    else:
        tree = None
    binary_tree(tree, 0)

    solution = Solution()
    print(solution.diameterOfBinaryTree(tree))
