class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False

            if rank[rootX] < rank[rootY]:
                rootX, rootY = rootY, rootX

            parent[rootY] = rootX
            rank[rootX] += rank[rootY]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]        