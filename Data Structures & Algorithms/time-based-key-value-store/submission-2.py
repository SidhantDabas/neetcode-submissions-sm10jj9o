class TimeMap:

    def __init__(self):
        self.table_time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table_time:
            self.table_time[key]=[]
        self.table_time[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        time = self.table_time.get(key,[])

        print(time)
        l, r = 0, len(time) - 1
        while l<=r:
            m = (l+r)//2
            if time[m][1] <= timestamp:
                res = time[m][0]
                print(res)
                l = m + 1
            else:
                r = m - 1
        return res



