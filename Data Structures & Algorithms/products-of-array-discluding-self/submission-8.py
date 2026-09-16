import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            count_zero = nums.count(0)
            if count_zero > 1:
                return [0 for _ in range(len(nums))]
            else:
                r = [0] * len(nums)
                j = 0
                temp = 1
                for i in range(len(nums)):
                    if nums[i] != 0:
                        temp *= nums[i]
                    else:
                        j = nums.index(nums[i])
                r[j] = temp
                return r
        else:
            temp = math.prod(nums)
            r = []
            for num in nums:
                r.append(temp // num)
            return r
        