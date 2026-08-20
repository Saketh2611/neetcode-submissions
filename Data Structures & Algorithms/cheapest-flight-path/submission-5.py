import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build Adjacency Graph
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
            
        # Priority Queue: (cost, node, stops_taken)
        # We sort by cost automatically
        pq = [(0, src, 0)]
        
        # Track minimum stops used to reach each node.
        # This is the key optimization:
        # If we reach a node again with MORE cost and MORE (or equal) stops, we discard it.
        # We only continue if we found a path with FEWER stops.
        min_stops = [float('inf')] * n
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            # If we reached destination, this is guaranteed to be the cheapest
            # valid path because it's a Min-Heap.
            if node == dst:
                return cost
            
            # If we have already exceeded max stops, drop this path
            # (We need <= k stops, meaning k+1 edges)
            if stops > k:
                continue
            
            # Optimization Pruning:
            # If we have visited this node before with fewer stops (or same stops),
            # and since Dijkstra ensures we visited it with lower/equal cost previously,
            # this current path is worse in every way. Skip it.
            if stops >= min_stops[node]:
                continue
            
            # Update the stops record for this node
            min_stops[node] = stops
            
            # Add neighbors
            for nei, w in adj[node]:
                heapq.heappush(pq, (cost + w, nei, stops + 1))
                
        return -1