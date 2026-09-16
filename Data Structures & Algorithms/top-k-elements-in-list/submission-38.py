import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_map = collections.Counter(nums)
        temp = []

        for num, f in c_map.items():
            heapq.heappush(temp, (f, num))

            if len(temp) > k:
                heapq.heappop(temp)
        r = []
        for f, num in temp:
            r.append(num)
        return r


        