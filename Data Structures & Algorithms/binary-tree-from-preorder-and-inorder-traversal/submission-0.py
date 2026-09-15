class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        index = inorder.index(preorder[0])

        root.left = self.buildTree(
            preorder[1:index + 1],
            inorder[:index]
        )

        root.right = self.buildTree(
            preorder[index + 1:],
            inorder[index + 1:]
        )

        return root

    def kthSmallest(self, root, k):
        stack = []
        current = root

        while current:
            stack.append(current)
            current = current.left

        while stack:
            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val

            current = current.right

            while current:
                stack.append(current)
                current = current.left