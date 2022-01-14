'''
Author: fghpdf
Date: 2022-01-14 09:14:30
LastEditTime: 2022-01-14 09:24:14
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 0:
            return heights

        res = [len(heights)-1]
        maxObu = heights[-1]
        for i in range(len(heights)-1,-1,-1):
            height = heights[i]
            if height > maxObu:
              maxObu = height
              res.append(i)
        
        res.reverse()
        return res

class TestSolution(unittest.TestCase):
    def testFindBuildings(self):
        sol = Solution()
        self.assertEqual(sol.findBuildings([4,2,3,1]), [0,2,3])
        self.assertEqual(sol.findBuildings([4,3,2,1]), [0,1,2,3])
        self.assertEqual(sol.findBuildings([1,3,2,4]), [3])

if __name__ == "__main__":
    unittest.main()