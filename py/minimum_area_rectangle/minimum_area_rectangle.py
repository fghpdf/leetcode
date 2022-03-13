import collections
from typing import List
import unittest

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) == 0:
          return 0

        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0

class TestSolution(unittest.TestCase):
    def testMinAreaRect(self):
        sol = Solution()
        self.assertEqual(sol.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]), 4)
        self.assertEqual(sol.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]), 2)

if __name__ == "__main__":
    unittest.main()