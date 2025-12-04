"""
- store key/value with additional timestamp
- when getting a value with corresponding key -> return latest timestamp at or prior to that value

loop from timestamp -> 0
{timestamp: {key, key, key}}
{key: value, key: value}


{key: [timestamps]} 
"foo": [1, 4, 12]

binary search -> look for first number smaller than 5
get("foo", 5) = 4
"""
class TimeMap:
    def __init__(self):
        self.map = {} # {key: {timestamp: value}}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return "" 
            
        timestamps = self.map[key]
        
        lo, hi = 0, len(timestamps) - 1
        res = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            if timestamps[mid][0] <= timestamp:
                lo = mid + 1
                res = timestamps[mid][1]
            else:
                hi = mid - 1

        return res



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)