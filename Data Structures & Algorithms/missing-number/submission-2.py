class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        r = n * (n + 1) // 2
        r = r - sum(nums)
        return r