'''
Author: fghpdf
Date: 2022-02-12 11:25:26
LastEditTime: 2022-02-12 11:40:50
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) == 0:
            return 0

        t = sorted(int(t[:2])*60+int(t[-2:]) for t in timePoints)
        t.append(t[0]+24*60)
        return min(b-a for a, b in zip(t, t[1:]))

class TestSolution(unittest.TestCase):
    def testFindMinDifference(self):
        sol = Solution()
        self.assertEqual(sol.findMinDifference(["23:59","00:00"]), 1)
        self.assertEqual(sol.findMinDifference(["00:00","23:59","00:00"]), 0)

if __name__ == '__main__':
    unittest.main()