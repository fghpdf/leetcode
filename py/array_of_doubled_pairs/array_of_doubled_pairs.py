import collections
from typing import List
import unittest

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        if len(arr) == 0:
          return False
        
        c = collections.Counter(arr)
        for x in sorted(c, key=abs):
          if c[x] > c[2*x]:
            return False
          c [2*x] -= c[x]

        return True

class TestSolution(unittest.TestCase):
    def testCanReorderDoubled(self):
        sol = Solution()
        self.assertEqual(sol.canReorderDoubled([3,1,3,6]), False)
        self.assertEqual(sol.canReorderDoubled([2,1,2,6]), False)
        self.assertEqual(sol.canReorderDoubled([4,-2,2,-4]), True)

if __name__ == '__main__':
  unittest.main()