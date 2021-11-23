from typing import List
import unittest

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
          i -= 1
        if i == 0: # nums are in descending order
            nums.reverse()
            return nums

        k = i - 1 # find the last "ascending" position
        while nums[j] <= nums[k]:
          j -= 1

        # swap
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1 # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
class TestSolution(unittest.TestCase):
    def testNextPermutation(self):
        sol = Solution()
        nums = [1,2,3]
        sol.nextPermutation(nums)
        self.assertEqual(nums, [1,3,2])
        nums = [3,2,1]
        sol.nextPermutation(nums)
        self.assertEqual(nums, [1,2,3])
        nums = [1,1,5]
        sol.nextPermutation(nums)
        self.assertEqual(nums, [1,5,1])
        nums = [1]
        sol.nextPermutation(nums)
        self.assertEqual(nums, [1])

if __name__ == '__main__':
    unittest.main()