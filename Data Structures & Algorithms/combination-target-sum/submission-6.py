class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []
        comb = []

        def dfs(i, total):
            if total == target:
                r.append(comb.copy())
                return
            if total > target:
                return
            
            for j in range(i, len(nums)):
                comb.append(nums[j])
                dfs(j, total + nums[j])

                comb.pop()
        dfs(0, 0)
        return r