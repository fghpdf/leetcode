'''
Author: fghpdf
Date: 2021-10-11 08:53:59
LastEditTime: 2021-10-11 20:25:48
LastEditors: fghpdf
'''
from functools import partial
from typing import List
from collections import deque
import unittest

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
      visited = set()
      q = deque()
      for i in range(len(mat)):
          for j in range(len(mat[0])):
              if mat[i][j] == 0:
                  visited.add((i,j))
                  q.append((i,j))
      
      while q:
          x,y = q.popleft()
          for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
              newX, newY = x+dirr[0], y+dirr[1]
              if newX >= 0 and newX <= len(mat)-1 and newY >= 0 and newY <= len(mat[0])-1 and (newX, newY) not in visited:
                      mat[newX][newY] = mat[x][y] + 1
                      visited.add((newX, newY))
                      q.append((newX, newY))
      return mat
    #   for i in range(len(mat)):
    #     for j in range(len(mat[i])):
    #       if mat[i][j] == 1:
    #         distance = self.BFSHelper(mat, i, j)
    #         mat[i][j] = distance

    #   return mat

    # def BFSHelper(self, mat: List[List[int]], row: int, col: int) -> int:
    #   q = deque()
    #   visited = set()

    #   # append start
    #   q.append((row, col))
    #   visited.add((row, col))
    #   step = 0

    #   dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    #   while q:
    #     for i in range(len(q)):
    #       cur = q.popleft()
    #       x, y = cur

    #       # judge
    #       if mat[x][y] == 0:
    #         return step

    #       # spread towards four directions
    #       for dir in dirs:
    #         newX, newY = x + dir[0], y + dir[1]
    #         # edge
    #         if newX >= 0 and newX < len(mat) and newY >= 0 and newY < len(mat[newX]):
    #           # not visit
    #           if (newX, newY) not in visited:
    #             q.append((newX, newY))
    #             visited.add((newX, newY))
                
    #     # update step
    #     step += 1
      
    #   return step


class TestUPdateMatrix(unittest.TestCase):
    def test_update_matrix(self):
      sol = Solution()
      self.assertEqual(sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]), [[0,0,0],[0,1,0],[0,0,0]])
      self.assertEqual(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]), [[0,0,0],[0,1,0],[1,2,1]])
      self.assertEqual(sol.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]), [[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])

if __name__ == '__main__':
    unittest.main()

    