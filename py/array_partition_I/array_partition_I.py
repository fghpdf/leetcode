from typing import List
import unittest

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        return sum(sorted(nums)[::2])

class TestSolution(unittest.TestCase):
    def testArrayPairSum(self):
        sol = Solution()
        self.assertEqual(sol.arrayPairSum([1,4,3,2]), 4)
        self.assertEqual(sol.arrayPairSum([6,2,6,5,1,2]), 9)

if __name__ == '__main__':
    unittest.main()