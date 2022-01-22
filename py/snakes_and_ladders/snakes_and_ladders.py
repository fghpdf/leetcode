'''
Author: fghpdf
Date: 2022-01-22 18:15:10
LastEditTime: 2022-01-22 18:25:28
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        need = {1:0}
        bfs = [1]

        for x in bfs:
          for i in range(x+1, x+7):
            a, b = (i-1)//n, (i-1)%n
            nxt = board[~a][b if a%2==0 else ~b]
            if nxt > 0:
              i = nxt
            if i == n*n:
              return need[x]+1
            if i not in need:
              need[i] = need[x]+1
              bfs.append(i)

        return -1

class TestSolution(unittest.TestCase):
    def testSnakesAndLadders(self):
        sol = Solution()
        self.assertEqual(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]), 4)
        self.assertEqual(sol.snakesAndLadders([[-1,-1],[-1,3]]), 1)

if __name__ == "__main__":
    unittest.main()