import unittest
import math

class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s) == 0:
            return 0

        charFrequency = {}
        for c in s:
          frequency = charFrequency.get(c, 0)
          charFrequency[c] = frequency + 1

        frequencySorted = sorted(charFrequency.values(), reverse=True)

        prev, keep = math.inf, 0
        for freq in frequencySorted:
          freq = min(prev - 1, freq)
          if freq == 0:
            break
          keep += freq
          prev = freq
        
        return len(s) - keep

class TestSolution(unittest.TestCase):
    def testMinDeletions(self):
        sol = Solution()
        self.assertEqual(sol.minDeletions("abb"), 0)
        self.assertEqual(sol.minDeletions("aaabbbcc"), 2)
        self.assertEqual(sol.minDeletions("ceabaacb"), 2)

if __name__ == "__main__":
    unittest.main()