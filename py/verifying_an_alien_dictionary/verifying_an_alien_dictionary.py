'''
Author: fghpdf
Date: 2022-01-06 09:11:12
LastEditTime: 2022-01-06 09:31:26
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 0 or len(order) == 0:
            return False

        orderDict = {}
        for i, o in enumerate(order):
          orderDict[o] = i

        for i in range(len(words) - 1):
          if not self.compareWords(words[i], words[i+1], orderDict):
              return False
        
        return True

    def compareWords(self, wordA: str, wordB: str, orderDict: dict) -> bool:
        aLength = len(wordA)
        bLength = len(wordB)
        
        for i in range(min(aLength, bLength)):
          if wordA[i] == wordB[i]:
              continue

          if orderDict[wordA[i]] > orderDict[wordB[i]]:
              return False
          else:
              return True

        return bLength >= aLength

class TestSolution(unittest.TestCase):
    def testIsAlienSorted(self):
        sol = Solution()
        self.assertEqual(sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"), True)
        self.assertEqual(sol.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"), False)
        self.assertEqual(sol.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"), False)
        self.assertEqual(sol.isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz"), True)

if __name__ == "__main__":
    unittest.main()