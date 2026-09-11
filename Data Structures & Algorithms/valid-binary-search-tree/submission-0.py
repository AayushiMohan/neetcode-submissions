class Solution:
    def isValidBST(self, root):
        def dfs(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (dfs(node.left, low, node.val) and
                    dfs(node.right, node.val, high))

        return dfs(root, float("-inf"), float("inf"))