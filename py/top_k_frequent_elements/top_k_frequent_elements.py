from typing import Counter, List
import unittest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
          return []

        numsCounter = Counter(nums)
        items = numsCounter.most_common(k)
        return [x for (x, y) in items]

class TestSolution(unittest.TestCase):
    def testTopKFrequent(self):
        sol = Solution()
        self.assertEqual(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2), [1,2])
        self.assertEqual(sol.topKFrequent(nums = [1], k = 1), [1])

if __name__ == '__main__':
    unittest.main()