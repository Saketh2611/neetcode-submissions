class Solution:
    def findRedundantConnection(self, edges):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False

            parent[pb] = pa
            return True

        # initialize
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v

            if not union(u, v):
                return [u, v]
