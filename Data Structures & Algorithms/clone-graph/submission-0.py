class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        cloned = {}

        def dfs(node):
            # Agar already clone bana hua hai
            if node in cloned:
                return cloned[node]

            # Current node ka clone banao
            copy = Node(node.val)
            cloned[node] = copy

            # Saare neighbors ko clone karo
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)