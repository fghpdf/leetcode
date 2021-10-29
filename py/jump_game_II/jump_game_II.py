from typing import List
import unittest

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        jumps = 0
        curEnd = 0
        curFasthest = 0

        for i in range(0, len(nums)-1):
            curFasthest = max(curFasthest, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = curFasthest
        
        return jumps

class TestSolution(unittest.TestCase):
    def testJump(self):
        sol = Solution()
        self.assertEqual(sol.jump([2,3,1,1,4]), 2)
        self.assertEqual(sol.jump([2,3,0,1,4]), 2)

if __name__ == '__main__':
    unittest.main()