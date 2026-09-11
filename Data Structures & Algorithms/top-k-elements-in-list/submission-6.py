import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq = collections.Counter(nums)
        vip_club = []
        for num, freq in dict_freq.items():
            heapq.heappush(vip_club, (freq, num))

            if len(vip_club) > k:
                heapq.heappop(vip_club)

        result = []
        for freq, num in vip_club:
            result.append(num)

        return result
