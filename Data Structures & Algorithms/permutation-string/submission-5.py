import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        fingerprint = collections.Counter(s1)
        c = collections.Counter(s2[:len(s1)])

        if fingerprint == c:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            c[s2[right]] = c.get(s2[right], 0) + 1
            c[s2[left]] -= 1
            if c[s2[left]] == 0:
                del c[s2[left]]
            left += 1
            if c == fingerprint:
                return True
        return False

        