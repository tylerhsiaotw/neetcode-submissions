class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = max_p = 0
        right = 1

        while right < len(prices):
            if prices[right] > prices[left]:
                max_p = max(max_p, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return max_p