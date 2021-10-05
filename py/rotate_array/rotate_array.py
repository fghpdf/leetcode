'''
Author: fghpdf
Date: 2021-10-05 09:29:54
LastEditTime: 2021-10-05 09:39:30
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]



class  TestRotateArray(unittest.TestCase):
  def test_rotate_array(self):
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    sol.rotate(nums, 3)
    self.assertEqual(nums, [5,6,7,1,2,3,4])
    nums = [1,2]
    sol.rotate(nums, 3)
    self.assertEqual(nums, [2,1])


if __name__ == '__main__':
    unittest.main()