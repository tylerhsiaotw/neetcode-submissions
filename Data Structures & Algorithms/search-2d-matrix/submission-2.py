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

            if target < matrix[row][col]:
                right = mid - 1
            elif target > matrix[row][col]:
                left = mid +  1
            else:
                return True
        return False 



        