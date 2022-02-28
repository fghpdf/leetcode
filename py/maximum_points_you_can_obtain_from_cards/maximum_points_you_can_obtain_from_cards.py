from typing import List
import unittest

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == 0 or len(cardPoints) < k:
            return 0
        
        size = len(cardPoints) - k
        minSubArraySum = float('inf')
        j = curr = 0

        for i, value in enumerate(cardPoints):
          curr += value
          if i - j + 1 > size:
            curr -= cardPoints[j]
            j += 1
        
          if i - j + 1 == size:
            minSubArraySum = min(minSubArraySum, curr)

        return sum(cardPoints) - minSubArraySum

class TestSolution(unittest.TestCase):
    def testMaxScore(self):
      sol = Solution()
      self.assertEqual(sol.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3), 12)
      self.assertEqual(sol.maxScore(cardPoints = [2,2,2], k = 2), 4)
      self.assertEqual(sol.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7), 55)

if __name__ == '__main__':
    unittest.main()