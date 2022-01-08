'''
Author: fghpdf
Date: 2022-01-08 20:42:01
LastEditTime: 2022-01-08 20:53:57
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) == 0:
            return 0

        # days is the number of bags
        left = 0
        right = 0

        for weight in weights:
            left = max(left, weight)
            right += weight

        while left < right:
            mid = (left + right) // 2
            actualDays = 1
            currentWeight = 0
            # put all items into the bags
            for weight in weights:
                if currentWeight + weight > mid:
                    currentWeight = 0
                    actualDays += 1
                currentWeight += weight
            
            if actualDays > days:
                left = mid + 1
            else:
                right = mid
        
        return left

class TestSolution(unittest.TestCase):
    def testShipWithinDays(self):
        sol = Solution()
        self.assertEqual(sol.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5), 15)
        self.assertEqual(sol.shipWithinDays(weights = [3,2,2,4,1,4], days = 3), 6)
        self.assertEqual(sol.shipWithinDays(weights = [1,2,3,1,1], days = 4), 3)

if __name__ == "__main__":
    unittest.main()