import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_map = collections.Counter(nums)

        temp = sorted(c_map.items(), key=lambda x : x[1], reverse=True)

        r = []

        for i in range(k):
                r.append(temp[i][0])

        return r
        