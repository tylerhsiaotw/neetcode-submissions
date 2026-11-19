class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []
        comb = []

        def dfs(i, total):
            if total == target:
                r.append(comb.copy())
                return 
            if total > target or i == len(nums):
                return
            
            comb.append(nums[i])
            dfs(i, total + nums[i])

            temp = comb.pop()

            dfs(i + 1, total)
        dfs(0, 0)
        return r
        