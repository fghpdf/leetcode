'''
Author: fghpdf
Date: 2022-02-02 10:55:17
LastEditTime: 2022-02-02 11:06:00
LastEditors: fghpdf
'''
from typing import List
import unittest
import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if len(arr) == 0:
            return 0

        countDict = collections.Counter(arr)
        sortedCount = sorted(countDict.items(), key=lambda pair:pair[1])

        for c in sortedCount:
          if k > 0 and k >= c[1]:
            k -= c[1]
            del countDict[c[0]]
          elif k > 0 and k < c[1]:
            k = 0

        return len(countDict.keys())



class TestSolution(unittest.TestCase):
    def testFindLeastNumOfUniqueInts(self):
        sol = Solution()
        self.assertEqual(sol.findLeastNumOfUniqueInts(arr = [5,5,4], k = 1), 1)
        self.assertEqual(sol.findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3), 2)

if __name__ == '__main__':
    unittest.main()