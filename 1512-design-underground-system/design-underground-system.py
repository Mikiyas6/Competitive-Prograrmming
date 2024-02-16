class UndergroundSystem:

    def __init__(self):
        
        self.hashmap1 = defaultdict(list)
        self.hashmap2 = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        self.hashmap1[id] = [stationName,t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        station1, time1 = self.hashmap1[id]

        self.hashmap2[station1+"->"+stationName].append(t - time1) 

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        times = self.hashmap2[startStation+"->"+endStation]
        
        total_time = sum(times)

        return total_time/len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)