'''
Author: fghpdf
Date: 2022-02-18 09:03:50
LastEditTime: 2022-02-18 09:50:36
LastEditors: fghpdf
'''
import collections
from typing import List
import unittest

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        if len(words) == 0:
            return 0

        wordDict = collections.defaultdict(list)
        count = 0
        for word in words:
          wordDict[word[0]].append(word)

        for char in s:
          wordsExpectingChar = wordDict[char]
          wordDict[char] = []
          for word in wordsExpectingChar:
            if len(word) == 1:
              count += 1
            else:
              wordDict[word[1]].append(word[1:])

        return count

class TestSolution(unittest.TestCase):
    def testNumMatchingSubseq(self):
        sol = Solution()
        self.assertEqual(sol.numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]), 3)
        self.assertEqual(sol.numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]), 2)

if __name__ == '__main__':
    unittest.main()