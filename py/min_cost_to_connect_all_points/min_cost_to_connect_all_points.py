import collections
import heapq
from typing import List
import unittest

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
          return 0

        manhattan = lambda p1, p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
          for j in range(i+1, n):
            d = manhattan(points[i], points[j])
            c[i].append((d, j))
            c[j].append((d, i))

        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
          d, j = heapq.heappop(heap)
          if not visited[j]:
            visited[j], cnt, ans = 1, cnt+1, ans+d
            for record in c[j]:
              heapq.heappush(heap, record)
          if cnt >= n:
            break
        return ans

class TestSolution(unittest.TestCase):
    def testMinCostConnectPoints(self):
        sol = Solution()
        self.assertEqual(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]), 20)
        self.assertEqual(sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]), 18)

if __name__ == '__main__':
    unittest.main()