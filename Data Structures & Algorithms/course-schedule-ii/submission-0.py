class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # FIX 1: correct edge direction
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        q = [i for i in range(numCourses) if indegree[i] == 0]
        ans = []
        visited = set()

        while q:
            node = q.pop(0)
            if node in visited:
                continue

            visited.add(node)
            ans.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # FIX 2: cycle check
        if len(ans) != numCourses:
            return []

        return ans
