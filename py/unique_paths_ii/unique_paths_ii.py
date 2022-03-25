from typing import List
import unittest

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
          return 0

        rowLen, colLen = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(colLen)] for _ in range(rowLen)]
        dp[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, rowLen):
          dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])

        for j in range(1, colLen):
          dp[0][j] = dp[0][j-1] * (1 - obstacleGrid[0][j])

        for i in range(1, rowLen):
          for j in range(1, colLen):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])

        return dp[-1][-1]

class TestSolution(unittest.TestCase):
    def testUniquePathsWithObstacles(self):
        sol = Solution()
        self.assertEqual(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]), 2)
        self.assertEqual(sol.uniquePathsWithObstacles([[0,1],[0,0]]), 1)
        self.assertEqual(sol.uniquePathsWithObstacles([[0],[0]]), 1)

if __name__ == '__main__':
    unittest.main()