from typing import List
import unittest

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        if len(board) == 0:
          return False

        xCount, oCount = 0, 0
        for i in range(len(board)):
          for j in range(len(board[i])):
            if board[i][j] == 'X':
              xCount += 1
            if board[i][j] == 'O':
              oCount += 1
        
        if oCount > xCount or xCount - oCount > 1:
          return False

        if self.check_win_positions(board, 'O'):
          if self.check_win_positions(board, 'X'):
            return False
          return oCount == xCount

        if self.check_win_positions(board, 'X') and xCount != oCount+1:
          return False

        return True

    def check_win_positions(self, board, player):
        # rows
        for i in range(len(board)):
          if board[i][0] == board[i][1] == board[i][2] == player:
            return True

        # cols
        for i in range(len(board)):
          if board[0][i] == board[1][i] == board[2][i] == player:
            return True

        # diagonals
        if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
            return True
        
        return False

class TestSolution(unittest.TestCase):
    def testValidTicTacToe(self):
        sol = Solution()
        self.assertEqual(sol.validTicTacToe(["O  ","   ","   "]), False)
        self.assertEqual(sol.validTicTacToe(["XOX"," X ","   "]), False)
        self.assertEqual(sol.validTicTacToe(["XOX","O O","XOX"]), True)

if __name__ == '__main__':
    unittest.main()