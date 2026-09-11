class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0

        for i in range(32):
            r <<= 1
            temp = n & 1
            r = r | temp
            n = n >> 1
        return r