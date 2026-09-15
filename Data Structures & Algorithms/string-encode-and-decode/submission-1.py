class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""

        for s in strs:
            n = str(len(s))
            temp += n + '#' + s

        return temp

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            start = j + 1
            end = j + 1 + length

            word = s[start : end]
            result.append(word)
            i = end
        return result


