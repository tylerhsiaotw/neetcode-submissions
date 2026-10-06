class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows = len(matrix)
        Cols = len(matrix[0])

        left = 0
        right = Rows * Cols - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // Cols
            col = mid % Cols
            val = matrix[row][col]
            
            if target < val:
                right = mid - 1
            elif target > val:
                left = mid + 1
            else:
                return True
        return False

        