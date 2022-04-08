import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      self.h = nums
      heapq.heapify(self.h)
      self.k = k
      while len(self.h) > k:
        heapq.heappop(self.h)

    def add(self, val: int) -> int:
      if len(self.h) < self.k:
        heapq.heappush(self.h, val)
      elif val > self.h[0]:
        heapq.heapreplace(self.h, val)
      return self.h[0]

s = KthLargest(3, [4, 5, 8, 2])
print(s.add(3))
print(s.add(5))
print(s.add(10))
print(s.add(9))
print(s.add(4))