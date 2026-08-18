class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}" : "{", "]" : "[", ")" : "("}

        for c in s:
            if c in mapping:
                if not stack:
                    return False

                top_item = stack.pop()

                if mapping[c] != top_item:
                    return False
            else:
                stack.append(c)
        return not stack