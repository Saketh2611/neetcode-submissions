class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        
        # 1. Generate all edges (same as your code)
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                # Store indices (i, j) instead of the points themselves to simplify Union-Find
                edges.append((dist, i, j))
        
        # 2. Sort edges by weight
        edges.sort() 
        
        # 3. Union-Find Setup
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # Path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                return True
            return False
        
        # 4. Kruskal's Algorithm
        mst_cost = 0
        edges_count = 0
        
        for dist, u, v in edges:
            if union(u, v):
                mst_cost += dist
                edges_count += 1
                # Optimization: If we have n-1 edges, we are done
                if edges_count == n - 1:
                    break
                    
        return mst_cost