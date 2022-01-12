'''
Author: fghpdf
Date: 2022-01-12 09:08:40
LastEditTime: 2022-01-12 09:17:09
LastEditors: fghpdf
'''
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.numDict = {}
        for i, n in enumerate(nums):
            self.numDict[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, n in vec.numDict.items():
            if i in self.numDict:
                res += self.numDict[i]*n

        return res