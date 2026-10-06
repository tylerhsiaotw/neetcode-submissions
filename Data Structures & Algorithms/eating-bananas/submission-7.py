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
                sum_h += math.ceil(p / mid)
            if sum_h <= h:
                r = mid
                right = mid - 1
            else:
                left = mid + 1
        return r

            