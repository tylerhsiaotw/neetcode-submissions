class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1] * len(nums)

        for i in range(1, len(nums)):
            r[i] = nums[i - 1] * r[i - 1]
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            r[i] *= temp
            temp *= nums[i]
        return r
        