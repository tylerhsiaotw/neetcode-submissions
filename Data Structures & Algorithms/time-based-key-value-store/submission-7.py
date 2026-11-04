import collections
class TimeMap:

    def __init__(self):
        self.timestamp = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        left = 0 
        right = len(self.timestamp[key]) - 1
        r = ""

        while left <= right:
            mid = (left + right) // 2
            if self.timestamp[key][mid][1] <= timestamp:
                r = self.timestamp[key][mid][0]
                left = mid + 1
            elif self.timestamp[key][mid][1] > timestamp:
                right = mid - 1
        return r

