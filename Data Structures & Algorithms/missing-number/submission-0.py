class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = 0
        n = len(nums)
        temp = [x for x in range(n + 1)]
        for num in nums:
            r = r ^ num
        for t in temp:
            r = r ^ t
        return r