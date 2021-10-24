'''
Author: fghpdf
Date: 2021-10-24 15:37:22
LastEditTime: 2021-10-24 16:30:56
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 0 or len(board[0]) <= 0:
            return

        # transfer edge O (connected) to *
        for row in range(len(board)):
            if board[row][0] == 'O':
              self.backtrack(board, row, 0)
            if board[row][len(board[0])-1] == 'O':
              self.backtrack(board, row, len(board[0])-1)

        for col in range(len(board[0])):
            if board[0][col] == 'O':
              self.backtrack(board, 0, col)
            if board[len(board)-1][col] == 'O':
              self.backtrack(board, len(board)-1, col)
        
        # all edge O is *
        # transfer * to O
        # transfer O to X
        for row in range(len(board)):
          for col in range(len(board[row])):
            if board[row][col] == 'O':
              board[row][col] = 'X'
            elif board[row][col] == '*':
              board[row][col] = 'O'

    def backtrack(self, board: List[List[str]], row, col):
      # edge
      if row < 0 or row > len(board)-1 or col < 0 or col > len(board[row])-1:
          return

      if board[row][col] == 'X':
          return

      if board[row][col] == '*':
          return

      if board[row][col] == 'O':
          board[row][col] = '*'

      self.backtrack(board, row+1, col)
      self.backtrack(board, row, col+1)
      self.backtrack(board, row-1, col)
      self.backtrack(board, row, col-1)
        

class TestSolution(unittest.TestCase):
    def testSolve(self):
        sol = Solution()
        board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
        sol.solve(board)
        self.assertEqual(board, [["X","O","X","O","X","O"],["O","X","X","X","X","X"],["X","X","X","X","X","O"],["O","X","O","X","O","X"]])
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        sol.solve(board)
        self.assertEqual(board, [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])
        board = [["X"]]
        sol.solve(board)
        self.assertEqual(board, [["X"]])
        board = [["O","O","O"],["O","O","O"],["O","O","O"]]
        sol.solve(board)
        self.assertEqual(board, [["O","O","O"],["O","O","O"],["O","O","O"]])
       

if __name__ == "__main__":
    unittest.main()