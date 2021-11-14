from typing import List
import unittest

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        n = len(nums)
        pos, neg = [0] * n, [0] * n
        if nums[0] > 0: pos[0] = 1
        if nums[0] < 0: neg[0] = 1
        ans = pos[0]
        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]
            ans = max(ans, pos[i])
        return ans


class TestSolution(unittest.TestCase):
    def testGetMaxLen(self):
        sol = Solution()
        self.assertEqual(sol.getMaxLen([1,-2,-3,4]), 4)
        self.assertEqual(sol.getMaxLen([0,1,-2,-3,-4]), 3)
        self.assertEqual(sol.getMaxLen([-1,-2,-3,0,1]), 2)
        self.assertEqual(sol.getMaxLen([-1,2]), 1)
        self.assertEqual(sol.getMaxLen([1,2,3,5,-6,4,0,10]), 4)

if __name__ == '__main__':
    unittest.main()
