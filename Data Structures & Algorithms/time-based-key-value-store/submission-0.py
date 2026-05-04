class TimeMap:

    def __init__(self):
        self.table_time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table_time:
            self.table_time[key] = {}
        if timestamp not in self.table_time[key]:
            self.table_time[key][timestamp] = []
        self.table_time[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table_time:
            return ""
        
        seen = 0

        for time in self.table_time[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.table_time[key][seen][-1]

