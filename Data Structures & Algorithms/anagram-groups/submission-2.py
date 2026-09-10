import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                i = ord(c) - ord('a')
                count[i] += 1
            fingerprint = tuple(count)

            anagram_map[fingerprint].append(s)
        return list(anagram_map.values())
        