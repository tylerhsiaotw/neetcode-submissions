class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num]+=1
        test = list(count.values())
        for t in test:
            if t != 1:
                return True
        return False
            
            
        