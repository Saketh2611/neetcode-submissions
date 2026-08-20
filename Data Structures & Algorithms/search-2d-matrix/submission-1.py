class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        up, down = 0, rows - 1

        # Step 1: Find the correct row
        while up <= down:
            mid_v = (up + down) // 2

            if target < matrix[mid_v][0]:
                down = mid_v - 1
            elif target > matrix[mid_v][cols - 1]:
                up = mid_v + 1
            else:
                # Step 2: Binary search in this row
                left, right = 0, cols - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[mid_v][mid] == target:
                        return True
                    elif target < matrix[mid_v][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False

        return False
