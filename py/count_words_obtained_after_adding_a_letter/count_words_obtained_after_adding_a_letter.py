from collections import defaultdict
from ctypes.wintypes import tagMSG
from typing import List
import unittest

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        if len(startWords) == 0 or len(targetWords) == 0:
          return 0

        def getHash(w: str) -> List[int]:
            h = [0] * 26
            for c in w:
                h[ord(c) - ord('a')] = 1
            return h

        groups = defaultdict(set)
        for w in startWords:
          h = getHash(w)
          groups[len(w)].add(tuple(h))

        cnt = 0
        for w in targetWords:
          if groups[len(w)-1]:
            h = getHash(w)
            for c in w:
              h[ord(c) - ord('a')] = 0
              if tuple(h) in groups[len(w) - 1]:
                  cnt += 1
                  break
              h[ord(c) - ord('a')] = 1

        return cnt

class TestSolution(unittest.TestCase):
    def testWordCount(self):
      sol = Solution()
      self.assertEqual(sol.wordCount(startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]), 2)
      self.assertEqual(sol.wordCount(startWords = ["ab","a"], targetWords = ["abc","abcd"]), 1)

if __name__ == "__main__":
  unittest.main()