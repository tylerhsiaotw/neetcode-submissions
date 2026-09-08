class Solution:
    def countBits(self, n: int) -> List[int]:
        def get_bits(i):
            count = 0
            while i > 0:
                if (i & 1) == 1:
                    count += 1
                i >>= 1

            return count

        lists = []
        for i in range(n + 1):
            x = get_bits(i)
            lists.append(x)


        return lists
        