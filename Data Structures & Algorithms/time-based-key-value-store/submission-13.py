import collections
class TimeMap:

    def __init__(self):
        self.timestamp = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        r = ""
        
        left = 0
        right = len(self.timestamp[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.timestamp[key][mid][1] == timestamp:
                return self.timestamp[key][mid][0]
            elif self.timestamp[key][mid][1] < timestamp:
                r = self.timestamp[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return r
                