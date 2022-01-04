'''
Author: fghpdf
Date: 2022-01-04 09:03:48
LastEditTime: 2022-01-04 09:12:43
LastEditors: fghpdf
'''
import unittest

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 0:
            return 0

        leftCount = 0
        rightCount = 0
        for c in s:
          if rightCount == 0 and c == ")":
            leftCount += 1
          else:
            rightCount += 1 if c == "(" else -1

        return leftCount + rightCount

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        sol = Solution()
        self.assertEqual(sol.minAddToMakeValid("())"), 1)
        self.assertEqual(sol.minAddToMakeValid("((("), 3)
        self.assertEqual(sol.minAddToMakeValid("()))(("), 4)

if __name__ == '__main__':
    unittest.main()