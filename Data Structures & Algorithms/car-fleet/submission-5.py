class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = []
        for i in range(len(speed)):
            p.append((position[i], speed[i]))
        p.sort(reverse=True)
        
        stack = []

        for i in range(len(speed)):
            time = (target - p[i][0]) / p[i][1]
            stack.append(time)

            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        