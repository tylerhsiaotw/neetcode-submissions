class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        fingerprint = {}
        for s in s1:
            fingerprint[s] = fingerprint.get(s, 0) + 1
        temp = s2[:len(s1)]
        count = {}
        for t in temp:
            count[t] = count.get(t, 0) + 1
        
        if count == fingerprint:
            return True

        left = 0
        for i in range(len(s1), len(s2)):
            count[s2[i]] = count.get(s2[i], 0) + 1
            count[s2[left]] -= 1
            if count[s2[left]] == 0:
                del count[s2[left]]

            left += 1
            if count == fingerprint:
                return True
        return False


        

        