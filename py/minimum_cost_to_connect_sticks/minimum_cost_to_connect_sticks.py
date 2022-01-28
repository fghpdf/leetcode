'''
Author: fghpdf
Date: 2022-01-28 09:09:49
LastEditTime: 2022-01-28 09:13:51
LastEditors: fghpdf
'''
import heapq
from typing import List
import unittest

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks)>1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            res += x+y
            heapq.heappush(sticks, x+y)
        return res

class TestSolution(unittest.TestCase):
    def testConnectSticks(self):
        sol = Solution()
        self.assertEqual(sol.connectSticks([2,4,3]), 14)
        self.assertEqual(sol.connectSticks([1,8,3,5]), 30)
        self.assertEqual(sol.connectSticks([5]), 0)

if __name__ == '__main__':
    unittest.main()