import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = collections.defaultdict(list)

        for s in strs:
            fingerprint = str(sorted(s))
            anagrams_dict[fingerprint].append(s)
        return list(anagrams_dict.values())

        