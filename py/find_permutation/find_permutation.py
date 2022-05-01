from typing import List
import unittest

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        if len(s) == 0:
          return []

        res = []
        startD = -1
        for i in range(len(s)):
          if s[i] == 'I':
            if startD != -1:
              res.extend(list(range(i+1, startD-1, -1)))
              startD = -1
            else:
              res.append(i+1)
          if s[i] == 'D' and startD == -1:
            startD = i+1
        
        if startD != -1:
          res.extend(list(range(len(s)+1, startD-1, -1)))
        else:
          res.extend(list(range(len(res)+1, len(s)+2)))
        return res


class TestSolution(unittest.TestCase):
    def testFindPermutation(self):
        sol = Solution()
        self.assertEqual(sol.findPermutation("I"), [1,2])
        self.assertEqual(sol.findPermutation("DIDDID"),  [2, 1, 5, 4, 3, 7, 6])
        self.assertEqual(sol.findPermutation("DI"), [2,1,3])
        self.assertEqual(sol.findPermutation("D"), [2,1])

if __name__ == '__main__':
    unittest.main()