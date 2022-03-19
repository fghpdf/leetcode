from typing import List
import unittest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
          return 0

        nums = set(nums)
        res = 0
        for num in nums:
          if num - 1 not in nums:
            begin = num + 1
            while begin in nums:
              begin += 1
            res = max(res, begin - num)
        
        return res

class TestSolution(unittest.TestCase):
    def testLongestConsecutive(self):
        sol = Solution()
        self.assertEqual(sol.longestConsecutive([100,4,200,1,3,2]), 4)
        self.assertEqual(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)

if __name__ == '__main__':
    unittest.main()