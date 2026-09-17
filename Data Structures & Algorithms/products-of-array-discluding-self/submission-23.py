import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            count_z = nums.count(0)
            if count_z > 1:
                return [0 for _ in range(len(nums))]
            else:
                temp = 1
                r = [0] * len(nums)
                j = 0
                for i in range(len(nums)):
                    if nums[i] == 0:
                        j = i
                    else:
                        temp *= nums[i]
                        r[i] = 0
                r[j] = temp
                return r
        else:
            p = math.prod(nums)
            r = []
            for num in nums:
                r.append(p // num)
            return r

                

        