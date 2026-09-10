class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        all = [x for x in range(n + 1)]
        r = 0
        for num in nums:
            r = r ^ num
        for a in all:
            r = r ^ a
        return r
        