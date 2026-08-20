class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        def bfs(x,y):
            visited = set()
            
            q = [(x,y,0)]
            while q : 
                x,y,cl = q.pop(0)
                visited.add((x,y))
                for dx,dy in directions :
                    if 0 <= x+dx < rows and 0 <= y+dy < cols:
                        if grid[x+dx][y+dy] != -1 and (x+dx,y+dy) not in visited :
                            if grid[x+dx][y+dy] == 0 :
                                return cl+1
                                break
                            q.append((x+dx,y+dy,cl+1))
                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == INF :
                    grid[i][j] = bfs(i,j)
        




        