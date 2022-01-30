'''
Author: fghpdf
Date: 2022-01-30 11:41:07
LastEditTime: 2022-01-30 11:53:17
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        if len(boxTypes) == 0:
            return 0

        boxTypes.sort(key=lambda tup: tup[1], reverse=True)
        
        res = 0
        for box in boxTypes:
          truckSize -= box[0]
          if truckSize > 0:
            res += box[0]*box[1]
          else:
            res += (truckSize+box[0]) * box[1]
            break
        return res


class TestSolution(unittest.TestCase):
    def testMaximumUnits(self):
        sol = Solution()
        self.assertEqual(sol.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4), 8)
        self.assertEqual(sol.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10), 91)

if __name__ == '__main__':
    unittest.main()