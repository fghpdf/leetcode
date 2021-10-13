'''
Author: fghpdf
Date: 2021-10-13 10:26:58
LastEditTime: 2021-10-13 11:06:45
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        track = ""
        res = []
        self.backtrack(s, track, res)
        return res

    def backtrack(self, s: str, track: str, res: List[str], pos = 0):
        # end
        if len(track) == len(s):
          res.append(track)
          return

        char = s[pos]
        if char.isalpha():
          self.backtrack(s, track + char.swapcase(), res, pos + 1)
        self.backtrack(s, track + char, res, pos + 1)

class TestLetterCasePermutation(unittest.TestCase):
    def test_letter_case_permutation(self):
        sol = Solution()
        self.assertEqual(sol.letterCasePermutation("a1b2"), ['A1B2', 'A1b2', 'a1B2', 'a1b2'])
        self.assertEqual(sol.letterCasePermutation("3z4"), ['3Z4', '3z4'])
        self.assertEqual(sol.letterCasePermutation("12345"), ["12345"])
        self.assertEqual(sol.letterCasePermutation("0"), ["0"])


if __name__ == '__main__':
    unittest.main()