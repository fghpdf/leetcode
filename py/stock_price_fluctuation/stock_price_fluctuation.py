from sortedcontainers import SortedDict

class StockPrice:

    def __init__(self):
      self.timeToPrices = SortedDict()
      self.rec = SortedDict()
        

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timeToPrices:
          prevPrice = self.timeToPrices[timestamp]
          self.rec[prevPrice].remove(timestamp)
          if len(self.rec[prevPrice]) == 0:
            self.rec.pop(prevPrice)
        if not price in self.rec:
          self.rec[price] = set()
        self.rec[price].add(timestamp)
        self.timeToPrices[timestamp] = price

    def current(self) -> int:
        return self.timeToPrices.peekitem(-1)[1]

    def maximum(self) -> int:
        return self.rec.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.rec.peekitem(0)[0]