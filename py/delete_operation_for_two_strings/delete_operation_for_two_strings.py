'''
Author: fghpdf
Date: 2021-11-02 09:20:49
LastEditTime: 2021-11-02 09:28:47
LastEditors: fghpdf
'''
import unittest
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return 0

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i, c in enumerate(word1):
            for j, d in enumerate(word2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])

        commonLen = dp[-1][-1]
        return len(word1) + len(word2) - 2*commonLen

class TestSolution(unittest.TestCase):
    def testMinDistance(self):
        sol = Solution()
        self.assertEqual(sol.minDistance(word1 = "sea", word2 = "eat"), 2)
        self.assertEqual(sol.minDistance(word1 = "leetcode", word2 = "etco"), 4)

if __name__ == '__main__':
    unittest.main()