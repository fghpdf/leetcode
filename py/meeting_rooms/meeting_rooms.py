from typing import List
import unittest

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
          return True

        intervals.sort()
        for i in range(1, len(intervals)):
          if intervals[i][0] < intervals[i-1][1]:
            return False

        return True


class TestSolution(unittest.TestCase):
    def testCanAttendMeetings(self):
      sol = Solution()
      self.assertEqual(sol.canAttendMeetings([[0,30],[5,10],[15,20]]), False)
      self.assertEqual(sol.canAttendMeetings([[7,10],[2,4]]), True)

if __name__ == '__main__':
    unittest.main()