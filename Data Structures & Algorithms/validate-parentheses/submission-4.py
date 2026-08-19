class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}" : "{", ")" : "(", "]" : "["}
        stack = []

        for string in s:
            if string not in mapping:
                stack.append(string)
            else:
                
                if not stack:
                    return False

                top_item = stack.pop()

                if top_item != mapping[string]:
                    return False
        return not stack
        