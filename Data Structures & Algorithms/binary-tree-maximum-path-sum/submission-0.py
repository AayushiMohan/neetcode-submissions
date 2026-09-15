class Solution:
    def maxPathSum(self, root):
        self.max_sum = float("-inf")

        def dfs(node):
            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path passing through current node
            current_path = node.val + left + right

            self.max_sum = max(self.max_sum, current_path)

            # Return one side only to parent
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum