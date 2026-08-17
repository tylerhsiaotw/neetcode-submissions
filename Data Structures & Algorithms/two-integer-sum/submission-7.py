class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}

        for i, num in enumerate(nums):
            remain = target - num

            if remain in history:
                return [history[remain], i]

            else:
                history[num] = i