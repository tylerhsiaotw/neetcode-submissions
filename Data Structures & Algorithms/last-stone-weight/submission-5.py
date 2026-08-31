class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while(len(stones) > 1):
            first = -heapq.heappop(stones)
            sec = -heapq.heappop(stones)
            if first == sec:
                continue
            elif first > sec:
                new_y = -abs(first - sec)
                heapq.heappush(stones, new_y)




        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
        