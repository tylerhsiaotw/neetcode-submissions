import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        r = []
        rr = []

        for x, y in points:
            dist = x**2 + y**2
            r.append([dist, x, y])
        heapq.heapify(r)

        for i in range(k):
            dist, x, y = heapq.heappop(r)
            rr.append([x, y])
        return rr

