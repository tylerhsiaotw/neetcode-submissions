import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        fingerprint = collections.Counter(s1)
        count = collections.Counter(s2[:len(s1)])

        if fingerprint == count:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            count[s2[right]] = count.get(s2[right], 0) + 1

            count[s2[left]] -= 1
            if count[s2[left]] == 0:
                del count[s2[left]]

            left += 1

            if fingerprint == count:
                return True
        return False
       
            

             