import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_map = collections.Counter(nums)

        temp = sorted(c_map.items(), key=lambda x : x[1], reverse=True)

        r = []

        for i in range(k):
            num, f = temp[i]
            r.append(num)

        return r
        