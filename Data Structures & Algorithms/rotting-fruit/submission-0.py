class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        timer = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def bfs(r, c):
            visited = set()
            queue = [(r, c)]
            timer[r][c] = 0

            while queue:
                x, y = queue.pop(0)
                visited.add((x, y))

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if (nx, ny) not in visited and grid[nx][ny] == 1:
                            timer[nx][ny] = min(timer[nx][ny], 1 + timer[x][y])
                            queue.append((nx, ny))
                            visited.add((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    timer[i][j] = 0
                elif grid[i][j] == 2:
                    bfs(i, j)

        max_time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and timer[i][j] == float('inf'):
                    return -1
                max_time = max(max_time, timer[i][j])

        return max_time
