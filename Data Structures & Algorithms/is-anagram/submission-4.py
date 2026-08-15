class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for s1 in s:
            if s1 not in dict1:
                dict1[s1] = 1
            else:
                dict1[s1] += 1
        for t1 in t:
            if t1 not in dict2:
                dict2[t1] = 1
            else:
                dict2[t1] += 1
        return dict2 == dict1
