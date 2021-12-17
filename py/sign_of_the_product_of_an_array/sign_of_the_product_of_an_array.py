from typing import List
import unittest

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        positiveCount = 0
        for num in nums:
            if num == 0:
                return 0
            if num > 0:
                positiveCount += 1
        
        if (len(nums) - positiveCount) % 2 == 0:
            return 1

        return -1

class TestSolution(unittest.TestCase):
    def testArraySign(self):
        sol = Solution()
        self.assertEqual(sol.arraySign([-1,-2,-3,-4,3,2,1]), 1)
        self.assertEqual(sol.arraySign([1,5,0,2,-3]), 0)
        self.assertEqual(sol.arraySign([-1,1,-1,1,-1]), -1)

if __name__ == '__main__':
    unittest.main()