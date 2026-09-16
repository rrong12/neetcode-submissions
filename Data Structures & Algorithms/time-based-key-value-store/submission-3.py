from collections import defaultdict 
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap[key]

        if arr is None:
            return ""

        l, r = 0, len(arr) - 1
        store = -1
        found = False

        while l <= r: 
            m = (l + r) // 2
            
            if arr[m][1] == timestamp:
                return arr[m][0]
        
            elif arr[m][1] > timestamp:
                r = m - 1
            
            else:
                store = m 
                l = m + 1
        
        if store > -1: return arr[store][0]
        else: return ""

            