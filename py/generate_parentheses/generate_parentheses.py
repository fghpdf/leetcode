'''
Author: fghpdf
Date: 2021-10-27 09:28:33
LastEditTime: 2021-10-27 09:44:40
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
          return []

        res = []
        self.backtrack(n, [], res, 0, 0)
        return res

    def backtrack(self, n, track: List[str], res: List[str], open: int, close: int):
      if len(track) == n*2:
        res.append(''.join(track[:]))
        return

      if open < n:
        # + (
        track.append("(")
        self.backtrack(n, track, res, open+1, close)
        track.pop()

      if close < open:
        # + )
        track.append(")")
        self.backtrack(n, track, res, open, close+1)
        track.pop()

class TestSolution(unittest.TestCase):
    def testGenerateParenthesis(self):
        sol = Solution()
        self.assertEqual(sol.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])
        self.assertEqual(sol.generateParenthesis(1), ["()"])

if __name__ == '__main__':
    unittest.main()