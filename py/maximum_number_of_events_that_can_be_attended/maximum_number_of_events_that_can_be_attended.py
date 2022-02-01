'''
Author: fghpdf
Date: 2022-02-01 10:07:44
LastEditTime: 2022-02-01 10:27:06
LastEditors: fghpdf
'''
import heapq
from typing import List
import unittest

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if len(events) == 0:
            return events

        events.sort(reverse=True)
        h = [] # event finish day
        res = 0
        day = 0
        while events or h:
          if not h:
            day = events[-1][0] # last event start day
          while events and events[-1][0] <= day:
            heapq.heappush(h, events.pop()[1])
          heapq.heappop(h)
          res += 1
          day += 1
          while h and h[0] < day:
            heapq.heappop(h)
        return res

class TestSolution(unittest.TestCase):
    def testMaxEvents(self):
        sol = Solution()
        self.assertEqual(sol.maxEvents([[1,2],[2,3],[3,4]]), 3)
        self.assertEqual(sol.maxEvents([[1,2],[2,3],[3,4],[1,2]]), 4)

if __name__ == '__main__':
    unittest.main()