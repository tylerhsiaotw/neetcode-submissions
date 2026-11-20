class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []
        comb = []
        nums.sort()

        def dfs(i, total):
            if total == target:
                r.append(comb.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                comb.append(nums[j])
                dfs(j, total + nums[j])
                comb.pop()
        dfs(0, 0)
        return r