'''
Author: fghpdf
Date: 2021-10-16 11:59:52
LastEditTime: 2021-10-16 12:04:12
LastEditors: fghpdf
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
          res ^= nums[i]

        return res