class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True

        seen = set()

        def get(x):
            total = 0
            while x > 0:
                digit = x % 10
                total += digit ** 2
                x = x // 10
            return total
        while n != 1:
            r = get(n)
            n = r
            if r in seen:
                return False
            else:
                seen.add(r)
        return True
        
        