'''
Author: fghpdf
Date: 2021-10-05 20:56:23
LastEditTime: 2021-10-05 21:10:46
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 2:
            return [1,2]

        for index in range(len(numbers)):
            num = numbers[index]
            if num <= target:
                try:
                    another_index = numbers.index(target - num, index+1)
                    return [index+1, another_index+1]
                except ValueError:
                    continue
            

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([2,7,11,15], 9), [1,2])
        self.assertEqual(sol.twoSum([2,3,4], 6), [1,3])
        self.assertEqual(sol.twoSum([-1,0], -1), [1,2])
        self.assertEqual(sol.twoSum([0,0,3,4], 0), [1,2])
        self.assertEqual(sol.twoSum([5,25,75],100), [2,3])

if __name__ == '__main__':
    unittest.main()