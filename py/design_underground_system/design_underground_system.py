from typing import Counter


class UndergroundSystem:

    def __init__(self):
        self.user = {}
        self.stationTime = Counter()
        self.stationFreq = Counter()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        endStation, startTime = self.user.pop(id)
        self.stationTime[(endStation, stationName)] += t - startTime
        self.stationFreq[(endStation, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stationTime[endStation, startStation] / self.stationFreq[endStation, startStation]