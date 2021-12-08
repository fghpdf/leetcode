from typing import List
import unittest

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        divider = [0] * len(arr)
        divider[0] = arr[0]

        for i in range(1, len(arr)):
          divider[i] = max(divider[i-1], arr[i])

        res = 0
        for i in range(len(arr)):
          if divider[i] == i:
            res += 1

        return res

class TestSolution(unittest.TestCase):
    def testMaxChunksToSorted(self):
        sol = Solution()
        self.assertEqual(sol.maxChunksToSorted([4,3,2,1,0]), 1)
        self.assertEqual(sol.maxChunksToSorted([1,0,2,3,4]), 4)

if __name__ == '__main__':
    unittest.main()