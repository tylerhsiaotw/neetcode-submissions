import collections
class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        left = 0
        right = len(self.store[key]) - 1
        r = ""

        while left <= right:
            mid = (left + right) // 2
            val = self.store[key][mid][0]

            if val > timestamp:
                right = mid - 1
            else:
                left = mid + 1
                r = self.store[key][mid][1]
        return r
        
