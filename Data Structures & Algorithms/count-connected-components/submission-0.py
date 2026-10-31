class Solution:
    def countComponents(self, n, edges):
        # Build adjacency list
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Check every node
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count        