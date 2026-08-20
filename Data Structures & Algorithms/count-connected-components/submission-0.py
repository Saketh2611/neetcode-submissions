class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        count = 0
        for u,v in edges :
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def bfs(node):
            queue = [node]
            visited.add(node)
            while queue : 
                n = queue.pop(0)
                for nei in adj[n]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i)
        return count
        