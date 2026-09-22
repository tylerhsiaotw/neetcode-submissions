class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        m = 0

        while left < right:
            m = max(m, (right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            elif  heights[left] > heights[right]:
                right -= 1               
            else:
                right -= 1
                left += 1
            
        return m        