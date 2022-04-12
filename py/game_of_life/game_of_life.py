from typing import List
import unittest

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
          return
        for row in range(len(board)):
          for col in range(len(board[row])):
            lives = self.poplutation(board, row, col)

            if board[row][col] == 0: 
                if lives == 3: board[row][col] = 2
            else:
                if lives < 2 or lives > 3: board[row][col] = 3

        for i in range(len(board)):
          for j in range(len(board[row])):
            if board[i][j] == 2: board[i][j] = 1
            if board[i][j] == 3: board[i][j] = 0

    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    def poplutation(self, board: List[List[int]], row: int, col: int) -> int:
      lives = 0
      for neighbor in self.neighbors:
        newRow = row+neighbor[0]
        newCol = col+neighbor[1]
        if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]):
          lives += board[newRow][newCol] % 2
      return lives

class TestSolution(unittest.TestCase):
    def testGameOfLife(self):
        sol = Solution()
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        sol.gameOfLife(board)
        self.assertEqual(board, [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])
        board = [[1,1],[1,0]]
        sol.gameOfLife(board)
        self.assertEqual(board, [[1,1],[1,1]])

if __name__ == '__main__':
    unittest.main()