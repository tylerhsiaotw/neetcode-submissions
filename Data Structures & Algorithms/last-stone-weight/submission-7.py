class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x == y:
                continue
            else:
                new_y = -abs(x - y)
                heapq.heappush(stones, new_y)

        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0
        