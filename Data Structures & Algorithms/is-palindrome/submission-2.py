class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        r = ""

        for c in s:
            if c.isalnum():
                r += c
        return r == r[::-1]