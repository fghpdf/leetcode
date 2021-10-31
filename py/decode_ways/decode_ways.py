'''
Author: fghpdf
Date: 2021-10-31 20:53:24
LastEditTime: 2021-10-31 21:04:31
LastEditors: fghpdf
'''
import unittest

class Solution:
    def numDecodings(self, s: str) -> int:
      if not s:
        return 0

      dp = [0] * (len(s)+1)

      dp[0] = 1
      dp[1] = 0 if s[0] == "0" else 1

      for i in range(2, len(s)+1):
        # 0 step jump
        if 0 < int(s[i-1:i]) <= 9:
            dp[i] += dp[i-1]
        # Two steps jump
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
      return dp[len(s)]
        
class TestSolution(unittest.TestCase):
    def testNumDecodings(self):
        sol = Solution()
        self.assertEqual(sol.numDecodings("12"), 2)
        self.assertEqual(sol.numDecodings("226"), 3)
        self.assertEqual(sol.numDecodings("0"), 0)
        self.assertEqual(sol.numDecodings("06"), 0)

if __name__ == "__main__":
    unittest.main()

