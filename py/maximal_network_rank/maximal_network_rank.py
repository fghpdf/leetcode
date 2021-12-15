from typing import List
import unittest

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if n == 0:
            return 0

        points = [0] * n
        connected = [[False for i in range(n)] for j in range(n)]

        for r in roads:
          points[r[0]] += 1
          points[r[1]] += 1
          connected[r[0]][r[1]] = True
          connected[r[1]][r[0]] = True

        res = 0
        for i in range(n):
          for j in range(i+1, n):
              line = 0
              # a line directly connects i and j, you will count roads[i, j] twice, so you have to remove 1
              if connected[i][j]:
                  line = 1
              res  = max(res, points[i] + points[j] - line)

        return res

class TestSolution(unittest.TestCase):
    def testMaximaNetworkRank(self):
        sol = Solution()
        self.assertEqual(sol.maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]]), 4)
        self.assertEqual(sol.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]), 5)
        self.assertEqual(sol.maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]), 5)

if __name__ == '__main__':
    unittest.main()