'''
Author: fghpdf
Date: 2021-10-14 09:21:41
LastEditTime: 2021-10-14 09:28:01
LastEditors: fghpdf
'''
import unittest

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0,1,2]
        for i in range(3, n+1):
          dp.append(dp[i-1] + dp[i-2])
        
        return dp[i]

class TestClimbStairs(unittest.TestCase):
    def test_climb_stairs(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(1), 1)
        self.assertEqual(sol.climbStairs(2), 2)
        self.assertEqual(sol.climbStairs(3), 3)

if __name__ == '__main__':
    unittest.main()