'''
Author: fghpdf
Date: 2022-01-23 14:02:31
LastEditTime: 2022-01-23 14:11:56
LastEditors: fghpdf
'''
import unittest

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = 0

        countOne = 0
        for i in range(len(s)):
          if s[i] == "1":
            countOne += 1
          else:
            res = min(countOne, res+1)
        return res

class TestSolution(unittest.TestCase):
    def testMinFlipsMonoIncr(self):
        sol = Solution()
        self.assertEqual(sol.minFlipsMonoIncr("00110"), 1)
        self.assertEqual(sol.minFlipsMonoIncr("010110"), 2)
        self.assertEqual(sol.minFlipsMonoIncr("00011000"), 2)

if __name__ == '__main__':
    unittest.main()
