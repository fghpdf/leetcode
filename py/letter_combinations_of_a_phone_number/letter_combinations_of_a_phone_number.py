'''
Author: fghpdf
Date: 2021-10-27 08:55:03
LastEditTime: 2021-10-27 09:19:45
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    speedDial = [
      [],
      [],
      ["a", "b", "c"],
      ["d", "e", "f"],
      ["g", "h", "i"],
      ["j", "k", "l"],
      ["m", "n", "o"],
      ["p", "q", "r", "s"],
      ["t", "u", "v"],
      ["w", "x", "y", "z"]
    ]
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
          return []

        res = []
        self.backtrack(digits, [], res, 0)
        return res

    def backtrack(self, digits: str, track: List[str], res: List[str], start):
        if len(track) == len(digits):
            res.append(''.join(track[:]))
            return

        index = int(digits[start])
        nums = self.speedDial[index]

        for n in nums:
          track.append(n)
          self.backtrack(digits, track, res, start+1)
          track.pop()
        


class TestSolution(unittest.TestCase):
    def testLetterCombinations(self):
        sol = Solution()
        self.assertEqual(sol.letterCombinations(digits = "23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(sol.letterCombinations(digits = ""), [])
        self.assertEqual(sol.letterCombinations(digits = "2"), ["a","b","c"])

if __name__ == '__main__':
    unittest.main()