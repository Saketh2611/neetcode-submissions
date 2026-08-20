class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if board[r][c] != 'O':
                return
            
            board[r][c] = '#'  # mark as safe
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # 1. Run DFS on boundary O's
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        
        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)

        # 2. Flip surrounded regions
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
