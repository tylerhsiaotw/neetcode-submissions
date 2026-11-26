import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        r = []
        res = []

        for x, y in points:
            dist = x**2 + y**2
            r.append((dist, x, y))

        heapq.heapify(r)

        for i in range(k):
            dist, x, y = heapq.heappop(r)
            res.append([x, y])
        return res




        