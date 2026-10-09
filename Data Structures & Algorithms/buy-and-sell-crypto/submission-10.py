class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = max_p = 0

        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                max_p = max(max_p, prices[right] - prices[left])
            else:
                left = right
        return max_p
        

        