class Solution:
    def countBits(self, n: int) -> List[int]:
        def getBits(n):
            count = 0
            while n > 0:
                if (n & 1) == 1:
                    count += 1
                n = n >> 1
            return count
        lists = []
        for i in range(n + 1):
            lists.append(getBits(i))
        return lists
        