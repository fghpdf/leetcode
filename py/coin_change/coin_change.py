'''
Author: fghpdf
Date: 2021-11-03 08:54:25
LastEditTime: 2021-11-03 09:02:18
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0:
            return 0

        # dp[i] = min(dp[i - coin] + 1).
        dp = [0] + [float('Inf') for i in range(amount)]
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                  dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[-1] == float('Inf'):
            return -1
        return dp[-1]

class TestSolution(unittest.TestCase):
    def testCoinChange(self):
        sol = Solution()
        self.assertEqual(sol.coinChange(coins = [1,2,5], amount = 11), 3)
        self.assertEqual(sol.coinChange(coins = [2], amount = 3), -1)
        self.assertEqual(sol.coinChange(coins = [1], amount = 0), 0)
        self.assertEqual(sol.coinChange(coins = [1], amount = 1), 1)
        self.assertEqual(sol.coinChange(coins = [1], amount = 2), 2)

if __name__ == '__main__':
    unittest.main()