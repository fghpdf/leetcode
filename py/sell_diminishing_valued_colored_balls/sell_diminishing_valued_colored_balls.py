'''
Author: fghpdf
Date: 2022-02-06 11:21:06
LastEditTime: 2022-02-06 11:48:44
LastEditors: fghpdf
'''
import heapq
from typing import List
import unittest

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        if len(inventory) == 0:
            return 0

        inventory.sort(reverse=True)
        inventory.append(0)
        ans, ind, width = 0,0,0

        while orders > 0:
          width += 1
          sell = min(orders, width*(inventory[ind]-inventory[ind+1]))
          whole, remainder = divmod(sell, width)
          ans += width*(whole*(inventory[ind]+inventory[ind]-(whole-1)))//2+remainder*(inventory[ind]-whole)
          orders-=sell
          ind += 1

        return ans%1_000_000_007


class TestSolution(unittest.TestCase):
    def testMaxProfit(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit(inventory = [2,5], orders = 4), 14)
        self.assertEqual(sol.maxProfit(inventory = [3,5], orders = 6), 19)

if __name__ == '__main__':
    unittest.main()