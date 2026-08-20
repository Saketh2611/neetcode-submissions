class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        max_area = 0
        def bfs(r,c):
            count = 1
            queue = [(r,c)]
            while queue : 
                x,y = queue.pop(0)
                visited.add((x,y))
                for dx,dy in directions :
                    nx,ny = x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols:
                        if (nx,ny) not in visited and grid[nx][ny] == 1:
                            count += 1
                            visited.add((nx,ny))
                            queue.append((nx,ny))
            return count 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = bfs(i,j)
                    if area > max_area :
                        max_area = area

        return max_area

                
                        
        