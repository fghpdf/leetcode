'''
Author: fghpdf
Date: 2021-10-04 22:07:55
LastEditTime: 2021-10-04 22:46:21
LastEditors: fghpdf
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
'''
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squareNumbs = []
        for num in nums:
          squareNumbs.append(num * num)

        squareNumbs.sort()
        return squareNumbs