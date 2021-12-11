from typing import List
import unittest

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) <= 4:
            return "Pending"

        # 0 is row 1, 3 is col 1, 6 is diagonal, 7 is anti diagonal 
        playerA = [0] * 8

        for i in range(len(moves)):
          row = moves[i][0]
          col = moves[i][1]

          change = -1
          if i % 2 == 0:
            change = 1
          playerA[row] += change
          playerA[col+3] += change
          if row == col:
            playerA[6] += change
          if row + col == 2:
            playerA[7] += change
          
        for i in playerA:
            if i == 3:
                return "A"
            if i == -3:
                return "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"

class TestSolution(unittest.TestCase):
    def testTictactoe(self):
        sol = Solution()
        self.assertEqual(sol.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]), "A")
        self.assertEqual(sol.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]), "B")
        self.assertEqual(sol.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]), "Draw")
        self.assertEqual(sol.tictactoe([[0,0],[1,1]]), "Pending")
        self.assertEqual(sol.tictactoe([[0,2],[1,0],[2,2],[1,2],[2,0],[0,0],[0,1],[2,1],[1,1]]), "A")

if __name__ == "__main__":
    unittest.main()