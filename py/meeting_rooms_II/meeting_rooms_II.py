from typing import List
import unittest
from functools import reduce

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = []
        ends = []
        for i in range(len(intervals)):
          starts.append(intervals[i][0])
          ends.append(intervals[i][1])

        starts.sort()
        ends.sort()

        rooms = 0
        endsItr = 0
        for i in range(len(starts)):
          if starts[i] < ends[endsItr]:
            rooms += 1
          else:
            endsItr += 1
        
        return rooms


    def intersection(self, rangeA: List[int], rangeB: List[int]) -> List[int]:
        if not rangeA or not rangeB:
            return None

        lowerA, upperA = rangeA[0], rangeA[1]
        lowerB, upperB = rangeB[0], rangeB[1]

        # A: [3,7] B:[1, 4]
        if lowerB < lowerA:
          if upperB < lowerA:
            return None
          if upperB < upperA:
            return [lowerA, upperB]
          # A: [3,7] B: [1,8]
          return rangeA[:]
        # A: [3,7] B:[6, 13]
        if lowerB < upperA:
          if upperB < upperA:
            return rangeB[:]
          return [lowerB, upperA]

        return None

class TestSolution(unittest.TestCase):
    def testMinMeetingRooms(self):
        sol = Solution()
        self.assertEqual(sol.minMeetingRooms([[0,30],[5,10],[15,20]]), 2)
        self.assertEqual(sol.minMeetingRooms([[7,10],[2,4]]), 1)

if __name__ == '__main__':
    unittest.main()