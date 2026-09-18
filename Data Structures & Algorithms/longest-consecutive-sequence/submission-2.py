class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hash_set = set(nums)
        m = 1

        for num in hash_set:
            if num - 1 in hash_set:
                continue
            c = 1
            while True:
                if num + 1 not in hash_set:
                    break
                else:
                    num += 1
                    c += 1
                    m = max(m, c)
        return m
            

        