'''
Author: fghpdf
Date: 2021-10-27 09:49:13
LastEditTime: 2021-10-27 10:08:51
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False

        for row in range(len(board)):
          for col in range(len(board[row])):
            if self.backtrack(board, word, 0, row, col):
                return True
        
        return False

    def backtrack(self, board: List[List[int]], word: str, resultIndex: int, row: int, col: int):
        if resultIndex == len(word):
            return True

        if row < 0 or col < 0 or row >= len(board) or col >= len(board[row]):
            return False

        if board[row][col] != word[resultIndex]:
            return False

        tmp = board[row][col]
        board[row][col] = '#'
        res = self.backtrack(board, word, resultIndex+1, row+1, col) or \
          self.backtrack(board, word, resultIndex+1, row, col+1) or \
            self.backtrack(board, word, resultIndex+1, row-1, col) or \
              self.backtrack(board, word, resultIndex+1, row, col-1)
        board[row][col] = tmp
        return res 


class TestSolution(unittest.TestCase):
    def testExist(self):
        sol = Solution()
        self.assertEqual(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"), True)
        self.assertEqual(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"), True)
        self.assertEqual(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"), False)

if __name__ == '__main__':
    unittest.main()
