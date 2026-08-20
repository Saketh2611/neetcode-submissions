class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        dp = [[-1]*cols for _ in range(rows)]
        
        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            
            best = 1  # path length starting from (r,c)
            
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            
            dp[r][c] = best
            return best
        
        maxi = 0
        for i in range(rows):
            for j in range(cols):
                maxi = max(maxi, dfs(i, j))
        
        return maxi
