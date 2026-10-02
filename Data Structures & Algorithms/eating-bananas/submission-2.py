import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        r = right

        while left <= right:
            mid = (left + right) // 2
            sum_h = 0
            for p in piles:
                t = math.ceil(p / mid)
                sum_h += t
            if sum_h > h:
                left = mid + 1
            elif sum_h <= h:
                right = mid - 1
                r = mid
        return r
            