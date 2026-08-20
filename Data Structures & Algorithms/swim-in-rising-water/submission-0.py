import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        pq = [(grid[0][0], 0, 0)]  # (max_height_so_far, x, y)
        visited = set()

        while pq:
            cost, x, y = heapq.heappop(pq)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if x == n-1 and y == n-1:
                return cost

            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    new_cost = max(cost, grid[nx][ny])
                    heapq.heappush(pq, (new_cost, nx, ny))
