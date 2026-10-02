class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWs = len(matrix)
        COLs = len(matrix[0])
        left = 0
        right = ROWs * COLs - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // COLs
            col = mid % COLs

            val = matrix[row][col]
            if val > target:
                right = mid - 1
            elif val < target:
                left = mid + 1
            else:
                return True
        return False

        