from typing import List
import unittest

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.getKth(nums1, nums2, l // 2)
        else:
            return (self.getKth(nums1, nums2, l // 2) + self.getKth(nums1, nums2, l // 2 - 1)) / 2

    def getKth(self, nums1: List[int], nums2: List[int], k: int) -> float:
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        mid1, mid2 = len(nums1) // 2, len(nums2) // 2

        if mid1 + mid2 < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if nums1[mid1] > nums2[mid2]:
                return self.getKth(nums1, nums2[mid2+1:], k - mid2 - 1)
            else:
                return self.getKth(nums1[mid1+1:], nums2, k - mid1 - 1)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.getKth(nums1[:mid1], nums2, k)
            else:
                return self.getKth(nums1, nums2[:mid2], k)

class TestSolution(unittest.TestCase):
    def testFindMedianSortedArrays(self):
      sol = Solution()
      self.assertEqual(sol.findMedianSortedArrays([1,2], [3]), 2.0)
      self.assertEqual(sol.findMedianSortedArrays([1,2], [3,4]), 2.5)

if __name__ == '__main__':
    unittest.main()
