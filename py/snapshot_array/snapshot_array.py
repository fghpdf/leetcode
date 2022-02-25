
import bisect


class SnapshotArray:

    def __init__(self, length: int):
      # snapId -> val 
      self.snaped = [[[-1, 0]] for _ in range(length)]
      self.snapNum = 0

    def set(self, index: int, val: int) -> None:
      self.snaped[index].append([self.snapNum, val])

    def snap(self) -> int:
      self.snapNum += 1
      return self.snapNum - 1

    def get(self, index: int, snap_id: int) -> int:
      i = bisect.bisect(self.snaped[index], [snap_id+1])-1
      return self.snaped[index][i][1]