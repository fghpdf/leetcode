from typing import List
import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        result = 0
        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result

class TestSolution(unittest.TestCase):
    def testMaxArea(self):
        sol = Solution()
        self.assertEqual(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(sol.maxArea([1,1]), 1)
        self.assertEqual(sol.maxArea([4,3,2,1,4]), 16)
        self.assertEqual(sol.maxArea([1,2,1]), 2)

if __name__ == '__main__':
    unittest.main()
