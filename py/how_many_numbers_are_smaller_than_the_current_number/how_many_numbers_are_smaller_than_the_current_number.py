from typing import List
import unittest

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return 0

        sortedNums = sorted(nums)

        m = {}
        for i, s in enumerate(sortedNums):
          if s not in m:
            m[s] = i

        res = [0] * len(nums)
        for i, n in enumerate(nums):
          count = m[n]
          res[i] = count

        return res



class TestSolution(unittest.TestCase):
    def testSmallerNumbersThanCurrent(self):
        sol = Solution()
        self.assertEqual(sol.smallerNumbersThanCurrent([8,1,2,2,3]), [4,0,1,1,3])
        self.assertEqual(sol.smallerNumbersThanCurrent([6,5,4,8]), [2,1,0,3])
        self.assertEqual(sol.smallerNumbersThanCurrent([7,7,7,7]), [0,0,0,0])

if __name__ == '__main__':
    unittest.main()