'''
Author: fghpdf
Date: 2021-10-05 19:53:28
LastEditTime: 2021-10-05 20:45:46
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
          return
        
        # count = 0
        # zero_index_list = []
        # for index in range(len(nums)):
        #   num = nums[index]
        #   if num == 0:
        #     zero_index_list.append(index)
        #     count = count + 1

        # zero_index_list.reverse()
        # for index in zero_index_list:
        #   nums.pop(index)

        # nums.extend([0] * count)
        position = 0
        for num in nums:
          if num != 0:
            # put no-zero element at front
            nums[position] = num
            position = position + 1

        # after position elements should be zero
        while position < len(nums):
          nums[position] = 0
          position = position + 1



class TestMoveZeros(unittest.TestCase):
  def test_move_zeros(self):
    sol = Solution()

    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    self.assertEqual(nums, [1,3,12,0,0])

    nums = [0,0,1]
    sol.moveZeroes(nums)
    self.assertEqual(nums, [1,0,0])


if __name__ == '__main__':
  unittest.main()