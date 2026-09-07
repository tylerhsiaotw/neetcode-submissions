class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        seen = set()

        def get(x):
            t = 0
            while x > 0:
                digit = x % 10
                t += digit ** 2
                x = x // 10
            return t

        while n != 1:
            r = get(n)
            if r == 1:
                return True

            if r in seen:
                return False
            else:
                seen.add(r)
                n = r
                

        

        