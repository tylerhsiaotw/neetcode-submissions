class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            n = str(len(s))
            r += n + '#' + s
        return r

    def decode(self, s: str) -> List[str]:
        i = 0
        r = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            n = int(s[i:j])
            start = j + 1
            end = j + 1 + n
            word = s[start:end]
            r.append(word)
            i = end
        return r

