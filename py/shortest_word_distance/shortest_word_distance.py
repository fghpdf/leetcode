from collections import defaultdict
from typing import List
import unittest

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if len(wordsDict) == 0:
          return 0

        indexDict = defaultdict(list)

        for i in range(len(wordsDict)):
          word = wordsDict[i]
          if word == word1 or word == word2:
            indexDict[word].append(i)

        print(indexDict)

        res = len(wordsDict)
        for i in indexDict[word1]:
          for j in indexDict[word2]:
            res = min(res, abs(i-j))

        return res 

class TestSolution(unittest.TestCase):
    def testShortestDistance(self):
        sol = Solution()
        self.assertEqual(sol.shortestDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"), 3)
        self.assertEqual(sol.shortestDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"), 1)

if __name__ == "__main__":
    unittest.main()