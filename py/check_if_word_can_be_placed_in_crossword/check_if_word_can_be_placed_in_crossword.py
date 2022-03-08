from typing import List
import unittest

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
          return False

        words = [word, word[::-1]]
        n = len(word)
        for B in board, zip(*board):
          for row in B:
            q = ''.join(row).split('#')
            for w in words:
              for s in q:
                if len(s) == n:
                  if all(s[i]==w[i] or s[i] == ' ' for i in range(n)):
                    return True
        
        return False

class TestSolution(unittest.TestCase):
    def testPlaceWordInCrossword(self):
        sol = Solution()
        self.assertEqual(sol.placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"), True)
        self.assertEqual(sol.placeWordInCrossword(board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"), False)
        self.assertEqual(sol.placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"), True)

if __name__ == '__main__':
    unittest.main()