class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""

        for string in s:
            if string.isalnum():
                r += string.lower()
                
        return r == r[::-1]
        