class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import heapq
        
        path = []
        adj = {}

        # Build adjacency (same as yours)
        for u, v in tickets:
            if u not in adj:
                adj[u] = []
            adj[u].append(v)

        # Convert lists to heaps (still your idea)
        for k in adj:
            heapq.heapify(adj[k])

        stack = ["JFK"]      # instead of queue

        while stack:
            node = stack[-1]

            # if no more outgoing edges → add to path
            if node not in adj or not adj[node]:
                path.append(stack.pop())
            else:
                # take smallest lexical neighbor
                next_node = heapq.heappop(adj[node])
                stack.append(next_node)

        return path[::-1]
