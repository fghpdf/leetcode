from typing import List
import unittest

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) == 0:
          return False

        color = {}
        def dfs(pos):
            for i in graph[pos]:
              if i in color:
                if color[i] == color[pos]:
                  return False
              else:
                color[i] = 1 - color[pos]
                if not dfs(i):
                  return False
            return True

        for i in range(len(graph)):
          if i not in color:
            color[i] = 0
            if not dfs(i):
              return False

        return True

class TestSolution(unittest.TestCase):
    def testIsBipartite(self):
        sol = Solution()
        self.assertEqual(sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]), False)
        self.assertEqual(sol.isBipartite([[1,3],[0,2],[1,3],[0,2]]), True)

if __name__ == '__main__':
    unittest.main()