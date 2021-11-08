from typing import List
import unittest

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        if len(nums1) == 0 or \
            len(nums2) == 0 or \
              len(nums3) == 0 or \
                len(nums4) == 0:
                return 0

        m = {}
        for index1 in range(len(nums1)):
          for index2 in range(len(nums2)):
            sum = nums1[index1] + nums2[index2]
            if not sum in m:
              m[sum] = 1
            else:
              m[sum] += 1

        res = 0
        for index3 in range(len(nums3)):
          for index4 in range(len(nums4)):
            sum = nums3[index3] + nums4[index4]
            if -sum in m:
              res += m[-sum]

        return res

    def backtrack(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int], res: List[List[int]],
      index1: int, index2: int, index3: int, index4: int):
        if index1 >= len(nums1) or index2 >= len(nums2) or index3 >= len(nums3) or index4 >= len(nums4):
          return
        if nums1[index1] + nums2[index2] + nums3[index3] + nums4[index4] == 0:
          res.append([index1, index2, index3, index4])


        
        return

class TestSolution(unittest.TestCase):
    def testFourSumCount(self):
        sol = Solution()
        self.assertEqual(sol.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]), 2)
        self.assertEqual(sol.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]), 1)

if __name__ == '__main__':
    unittest.main()