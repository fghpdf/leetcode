'''
Author: fghpdf
Date: 2022-02-17 08:55:08
LastEditTime: 2022-02-17 09:03:07
LastEditors: fghpdf
'''
import unittest

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
      if len(start) != len(end):
        return False

      startLR = [(s,idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
      endLR = [(e, idx) for idx, e in enumerate(end) if e == 'L' or e == 'R']

      if len(startLR) != len(endLR):
        return False

      for (s, i), (e, j) in zip(startLR, endLR):
        if s != e:
          return False
        if s == 'L':
          if i < j:
            return False
        if e == 'R':
          if i > j:
            return False

      return True

class TestSolution(unittest.TestCase):
    def testCanTransform(self):
      sol = Solution()
      self.assertEqual(sol.canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"), True)
      self.assertEqual(sol.canTransform(start = "X", end = "L"), False)

if __name__ == '__main__':
    unittest.main()