from typing import List
import unittest
from unittest import result

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 0:
          return 0

        dp = {}
        result = 1

        for word in sorted(words, key=len):
          dp[word] = 1

          # loop all possible sub word
          for i in range(len(word)):
            prevWord = word[:i]+word[i+1:]

            if prevWord in dp:
              dp[word] = max(dp[prevWord]+1, dp[word])
              result = max(result, dp[word])

        return result

class TestSolution(unittest.TestCase):
    def testLongestStrChain(self):
        sol = Solution()
        self.assertEqual(sol.longestStrChain(["a","b","ba","bca","bda","bdca"]), 4)
        self.assertEqual(sol.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]), 5)
        self.assertEqual(sol.longestStrChain(["abcd","dbqca"]), 1)

if __name__ == "__main__":
    unittest.main()