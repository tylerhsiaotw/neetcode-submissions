import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = collections.defaultdict(list)

        for s in strs:

            count = [0] * 26
            for char in s:
                i = ord(char) - ord('a')
                count[i] += 1
            anagram_map[tuple(count)].append(s)
        return list(anagram_map.values())