'''
Author: fghpdf
Date: 2021-11-02 08:57:10
LastEditTime: 2021-11-02 09:14:51
LastEditors: fghpdf
'''
import unittest

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]

class TestSolution(unittest.TestCase):
    def testLongestCommonSubsequence(self):
        sol = Solution()
        self.assertEqual(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace"), 3)
        self.assertEqual(sol.longestCommonSubsequence(text1 = "abc", text2 = "abc"), 3)
        self.assertEqual(sol.longestCommonSubsequence(text1 = "abc", text2 = "def"), 0)

if __name__ == '__main__':
    unittest.main()        