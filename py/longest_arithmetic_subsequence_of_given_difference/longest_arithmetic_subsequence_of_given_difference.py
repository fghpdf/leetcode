from typing import List
import unittest

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if len(arr) == 0:
          return 0

        res = {}
        for num in arr:
          if num - difference in res:
            res[num] = res[num-difference]+1
          else:
            res[num] = 1
        return max(res.values())        

class TestSolution(unittest.TestCase):
    def  testLongestSubsequence(self):
        sol = Solution()
        self.assertEqual(sol.longestSubsequence(arr = [1,2,3,4], difference = 1), 4)
        self.assertEqual(sol.longestSubsequence(arr = [1,3,5,7], difference = 1), 1)
        self.assertEqual(sol.longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2), 4)

if __name__ == '__main__':
    unittest.main()