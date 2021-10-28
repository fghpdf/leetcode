from typing import List
import unittest

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.backtrack(nums, 0, len(nums)-2), self.backtrack(nums, 1, len(nums)-1))

    def backtrack(self, nums: List[int], low: int, high: int) -> int:
        include = 0
        exclude = 0
        for j in range(low, high+1):
            iTemp = include
            eTemp = exclude
            include = eTemp + nums[j]
            exclude = max(iTemp, eTemp)

        return max(include, exclude)            


class TestSolution(unittest.TestCase):
    def testRob(self):
        sol = Solution()
        self.assertEqual(sol.rob([2,3,2]), 3)
        self.assertEqual(sol.rob([1,2,3,1]), 4)

if __name__ == '__main__':
    unittest.main()
