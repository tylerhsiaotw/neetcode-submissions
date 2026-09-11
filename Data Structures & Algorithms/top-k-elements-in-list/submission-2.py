import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq = collections.defaultdict(int)

        for num in nums:
            dict_freq[num] += 1
        sorted_items = sorted(dict_freq.items(), key= lambda  x : x[1], reverse=True)
        r = []
        for i in range(k):
            r.append(sorted_items[i][0])
        return r


        