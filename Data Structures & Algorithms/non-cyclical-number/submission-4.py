class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        def get_next(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n = n // 10
            return total
        
        while n != 1:
            r = get_next(n)
            if r in seen:
                return False
            seen.add(r)
            n = r
        return True
        

        