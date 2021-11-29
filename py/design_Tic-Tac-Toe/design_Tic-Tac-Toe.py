from typing import List
import unittest

class TicTacToe:
    rows: List[int]
    cols: List[int]
    diagonal: int
    antiDiagonal: int

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        toAdd = 1 if player == 1 else -1

        self.rows[row] += toAdd
        self.cols[col] += toAdd

        if row == col:
          self.diagonal += toAdd

        if col == len(self.cols) - row - 1:
          self.antiDiagonal += toAdd

        size = len(self.rows)
        if abs(self.rows[row]) == size or \
          abs(self.cols[col]) == size or \
            abs(self.diagonal) == size or \
              abs(self.antiDiagonal) == size:
              return player

        return 0



class TestSolution(unittest.TestCase):
    def testTicTacToe(self):
      t = TicTacToe(3)
      self.assertEqual(t.move(0, 0, 1), 0)
      self.assertEqual(t.move(0, 2, 2), 0)
      self.assertEqual(t.move(2, 2, 1), 0)
      self.assertEqual(t.move(1, 1, 2), 0)
      self.assertEqual(t.move(2, 0, 1), 0)
      self.assertEqual(t.move(1, 0, 2), 0)
      self.assertEqual(t.move(2, 1, 1), 1)


if __name__ == '__main__':
    unittest.main()