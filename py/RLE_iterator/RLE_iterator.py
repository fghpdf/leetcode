from typing import List


class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.numbers = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while (self.index < len(self.numbers)):
          if n <= self.numbers[self.index]:
            self.numbers[self.index] -= n
            return self.numbers[self.index+1]
          n -= self.numbers[self.index]
          self.index += 2
        
        return -1


# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator([3, 8, 0, 9, 2, 5])
print(obj.next(2))
print(obj.next(1))
print(obj.next(1))
print(obj.next(2))

