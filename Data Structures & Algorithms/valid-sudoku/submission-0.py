class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        cols = 9

        # 1. CHECK ROWS
        for r in range(rows):
            visited = set()
            for c in range(cols):
                val = board[r][c]  # FIX: Get the actual value
                if val == '.':
                    continue
                
                if val in visited:
                    return False
                visited.add(val)

        # 2. CHECK COLUMNS
        for c in range(cols):
            visited = set()
            for r in range(rows):
                val = board[r][c]  # FIX: Get the actual value
                if val == '.':
                    continue
                
                if val in visited:
                    return False
                visited.add(val)

        # 3. CHECK 3x3 SUB-BOXES (The missing part)
        # We jump 3 steps at a time to land on the top-left of each box
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                visited = set()
                # Iterate through the 3x3 grid starting at [r][c]
                for i in range(3):
                    for j in range(3):
                        val = board[r + i][c + j]
                        if val == '.':
                            continue
                        
                        if val in visited:
                            return False
                        visited.add(val)

        return True