class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        l = 0
        existed = set()

        for right in range(len(s)):
            while s[right] in existed:
                existed.remove(s[left])
                left += 1
            existed.add(s[right])
            l = max(l, right - left + 1)
        return l
        