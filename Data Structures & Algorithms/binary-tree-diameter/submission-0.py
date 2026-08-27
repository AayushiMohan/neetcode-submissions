class Solution:
    def diameterOfBinaryTree(self, root):

        diameter = 0

        def depth(node):
            nonlocal diameter

            if node is None:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        depth(root)

        return diameter
        