'''
Author: fghpdf
Date: 2021-10-11 20:22:39
LastEditTime: 2021-10-11 21:19:16
LastEditors: fghpdf
'''
from typing import Deque, List
import unittest

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = Deque()

        step = 0
        freshCount = 0
        # append start
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    visited.add((i, j))
                    q.append((i, j))

        if freshCount == 0:
            return 0

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            for index in range(len(q)):
                x, y = q.popleft()
                for dir in dirs:
                    newX, newY = x+dir[0], y+dir[1]

                    # edge
                    if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[newX]):
                        continue

                    # 0 is empty
                    if grid[newX][newY] == 0:
                        continue

                    if (newX, newY) not in visited and grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        visited.add((newX, newY))
                        q.append((newX, newY))

            # step ++
            step += 1

        # check
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        # last time is all fresh to rotten
        return step - 1


class TestOrangesRotting(unittest.TestCase):
    def test_oranges_rotting(self):
      sol = Solution()
      self.assertEqual(sol.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]), 2)
      self.assertEqual(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]), 4)
      self.assertEqual(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]), -1)
      self.assertEqual(sol.orangesRotting([[0,2]]), 0)

if __name__ == '__main__':
    unittest.main()