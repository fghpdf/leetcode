from typing import List
import unittest

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
          return []

        res = [x for x in range(1, len(nums)+1)]
        res = set(res)
        for i in range(len(nums)):
          if nums[i] in res:
            res.remove(nums[i])

        return list(res)

class TestSolution(unittest.TestCase):
    def testFindDisappeareNumbers(self):
       sol = Solution()
       self.assertEqual(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]), [5,6])
       self.assertEqual(sol.findDisappearedNumbers([1,1]), [2])

if __name__ == '__main__':
  unittest.main()