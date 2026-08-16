class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for d_t in t:
            if d_t in dict1:
                dict1[d_t] += 1
            else:
                dict1[d_t] = 1

        for d_s in s:
            if d_s in dict2:
                dict2[d_s] += 1
            else:
                dict2[d_s] = 1

        return dict1 == dict2