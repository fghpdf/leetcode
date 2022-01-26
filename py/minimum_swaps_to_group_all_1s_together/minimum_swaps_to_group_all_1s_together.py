'''
Author: fghpdf
Date: 2022-01-26 09:20:47
LastEditTime: 2022-01-26 09:25:22
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        if len(data) == 0:
            return 0

        width, maxWin, cntWin, l = sum(data), 0, 0, -1
        for r, d in enumerate(data):
            cntWin += d
            if r-l > width:
              l += 1
              cntWin -= data[l]
            maxWin = max(maxWin, cntWin)
        return width-maxWin
        
class TestSolution(unittest.TestCase):
    def testMinSwaps(self):
        sol = Solution()
        self.assertEqual(sol.minSwaps([1,0,1,0,1]), 1)
        self.assertEqual(sol.minSwaps([0,0,0,1,0]), 0)
        self.assertEqual(sol.minSwaps([1,0,1,0,1,0,0,1,1,0,1]), 3)

if __name__ == '__main__':
    unittest.main()