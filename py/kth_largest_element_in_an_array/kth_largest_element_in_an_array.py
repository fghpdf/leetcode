import heapq
from typing import List
import unittest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      if len(nums) == 0:
        return 0
      
      # convert to smaller
      k = len(nums) - k
      left = 0
      right = len(nums) - 1

      while left < right:
        pivot = self.partition(nums, left, right)
        if pivot == k:
          break

        if pivot < k:
          left = left + 1
        elif pivot > k:
          right = right - 1

      return nums[k]

    def partition(self, nums: List[int], left: int, right: int) -> int:
      # choose the right-most element as pivot
      low = left
      while left < right:
        if nums[left] < nums[right]:
          # left of low is smaller one
          nums[left], nums[low] = nums[low], nums[left]
          low += 1
        left += 1
      nums[right], nums[low] = nums[low], nums[right]
      return low

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     if len(nums) == 0:
    #       return 0

    #     heap = []
    #     for n in nums:
    #       heapq.heappush(heap, n)

    #       if len(heap) > k:
    #         heapq.heappop(heap)

    #     return heapq.heappop(heap)

class TestSolution(unittest.TestCase):
    def testFIndKthLargest(self):
      sol = Solution()
      self.assertEqual(sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2), 5)
      self.assertEqual(sol.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4), 4)

if __name__ == '__main__':
    unittest.main()