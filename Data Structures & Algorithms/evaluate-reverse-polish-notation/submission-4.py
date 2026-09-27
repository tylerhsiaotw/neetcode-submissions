class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            r = 0
            if t in op:
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    r = b + a
                elif t == "-":
                    r = b - a
                elif t == "*":
                    r = b * a
                elif t == "/":
                    r = int(b / a)
                stack.append(r)               
            else:
                stack.append(int(t))
        return stack[0]

        