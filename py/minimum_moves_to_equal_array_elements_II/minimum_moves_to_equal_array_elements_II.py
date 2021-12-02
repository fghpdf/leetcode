from typing import List
import unittest

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        head = 0
        tail = len(nums) - 1
        res = 0
        while head < tail:
          res += nums[tail] - nums[head]
          head += 1
          tail -= 1
        
        return res

class TestSolution(unittest.TestCase):
    def testMinMoves2(self):
        sol = Solution()
        self.assertEqual(sol.minMoves2([1,2,3]), 2)
        self.assertEqual(sol.minMoves2([1,10,2,9]), 16)

if __name__ == '__main__':
    unittest.main()