'''
Author: fghpdf
Date: 2022-02-13 10:40:31
LastEditTime: 2022-02-13 11:23:18
LastEditors: fghpdf
'''
import collections
from typing import List
import unittest

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if len(mat) == 0:
            return 0

        maxlen = 0
        currLen = collections.Counter()
        for i, row in enumerate(mat):
            for j, a in enumerate(row):
                for key in i, j+.1, i+j+.2, i-j+.3:
                    currLen[key] = (currLen[key] + 1) * a
                    maxlen = max(maxlen, currLen[key])
        return maxlen

class TestSolution(unittest.TestCase):
    def testLongestLine(self):
        sol = Solution()
        self.assertEqual(sol.longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]), 3)
        self.assertEqual(sol.longestLine([[1,1,1,1],[0,1,1,0],[0,0,0,1]]), 4)

if __name__ == '__main__':
    unittest.main()