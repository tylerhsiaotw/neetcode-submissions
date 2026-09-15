import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_map = collections.defaultdict(int)

        for num in nums:
            c_map[num] += 1
        r = []
        for num, f in c_map.items():
            heapq.heappush(r, (f, num))

            if len(r) > k:
                heapq.heappop(r)

        result = []

        for f, num in r:
            result.append(num)
        return result
            
