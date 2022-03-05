from collections import defaultdict
from email.policy import default
from typing import Counter, List


class DetectSquares:

    def __init__(self):
        self.d = Counter()
        self.x_coord = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.d[x,y] += 1
        self.x_coord[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for y2 in self.x_coord[x]:
          if y2 == y: continue
          ans += self.d[x, y2] * self.d[x+y2-y, y] * self.d[x+y2-y, y2]
          ans += self.d[x, y2] * self.d[x+y-y2, y] * self.d[x+y-y2, y2]
        return ans

        