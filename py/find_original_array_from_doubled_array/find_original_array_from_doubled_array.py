import collections
from typing import List
import unittest

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) == 0:
          return []

        c = collections.Counter(changed)
        if c[0] % 2:
          return []
        for x in sorted(c):
          if c[x] > c[2*x]:
            return []
          c[2*x] -= c[x] if x else c[x]//2
        
        return list(c.elements())

class TestSolution(unittest.TestCase):
    def testFindOriginalArray(self):
        sol = Solution()
        self.assertEqual(sol.findOriginalArray([1,3,4,2,6,8]), [1,3,4])
        self.assertEqual(sol.findOriginalArray([6,3,0,1]), [])
        self.assertEqual(sol.findOriginalArray([1]), [])
        self.assertEqual(sol.findOriginalArray([0,0,0,0]), [0,0])

if __name__ == '__main__':
    unittest.main()