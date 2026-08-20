class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        maxi = 0
        
        def dfs(r, c, prev):
            # boundary or not increasing
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev:
                return 0
            
            best = 0
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                best = max(best, dfs(nr, nc, matrix[r][c]))
            
            return 1 + best
        
        for i in range(rows):
            for j in range(cols):
                maxi = max(maxi, dfs(i, j, -1))
        
        return maxi
