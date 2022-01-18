'''
Author: fghpdf
Date: 2022-01-18 08:51:46
LastEditTime: 2022-01-18 08:56:13
LastEditors: fghpdf
'''
import unittest

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 0:
            return s

        groupCount = 1
        preCount = 0
        res = 0
        for i in range(len(s)-1):
          if s[i] == s[i+1]:
              groupCount += 1
          else:
              res += min(preCount, groupCount)
              preCount = groupCount
              groupCount = 1

        return res + min(preCount, groupCount)

class TestSolution(unittest.TestCase):
    def testCountBinarySubstrings(self):
        sol = Solution()
        self.assertEqual(sol.countBinarySubstrings("00110011"), 6)
        self.assertEqual(sol.countBinarySubstrings("10101"), 4)

if __name__ == '__main__':
    unittest.main()