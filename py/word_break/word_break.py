'''
Author: fghpdf
Date: 2021-10-31 21:16:50
LastEditTime: 2021-10-31 21:32:00
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
          return False

        isSubWordBreak = [False for n in range(len(s)+1)]

        isSubWordBreak[0] = True
        for i in range(1, len(s)+1):
          for j in range(0, i):
            if isSubWordBreak[j] and s[j:i] in wordDict:
                isSubWordBreak[i] = True
                break

        return isSubWordBreak[len(s)]

class TestSolution(unittest.TestCase):
    def testWordBreak(self):
        sol = Solution()
        self.assertEqual(sol.wordBreak(s = "leetcode", wordDict = ["leet","code"]), True)
        self.assertEqual(sol.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]), True)
        self.assertEqual(sol.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]), False)

if __name__ == '__main__':
    unittest.main()