class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]

        # Binary Search for largest timestamp <= given timestamp
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]

            if arr[mid][0] < timestamp:
                res = arr[mid][1]   # possible answer
                l = mid + 1
            else:
                r = mid - 1

        return res
