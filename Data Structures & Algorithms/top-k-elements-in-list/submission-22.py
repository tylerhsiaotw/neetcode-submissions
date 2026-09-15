import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_map = collections.defaultdict(int)
        for num in nums:
            c_map[num] += 1
        temp = [[] for _ in range(len(nums) + 1)]
        for num, f in c_map.items():
            temp[f].append(num)

        r = []
        for i in range(len(temp) - 1, 0, -1):
            for num in temp[i]:
                r.append(num)

                if len(r) == k:
                    return r

