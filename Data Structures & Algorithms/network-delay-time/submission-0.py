import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u,v,t in times :
            adj[u].append((v,t))
        cost = [float('inf')]*(n+1)
        cost[0] = 0
        cost[k] = 0
        heap = [(k,0)]
        visited = set()
        visited.add(k)
        while heap : 
            node,c_c = heapq.heappop(heap)
            for nei,t_t in adj[node] :
                if nei not in visited and cost[nei] > t_t + c_c :
                    cost[nei] = t_t + c_c
                    heapq.heappush(heap,(nei,cost[nei]))
        if max(cost) == float('inf') :
            return -1 
        else : 
            return max(cost)

        