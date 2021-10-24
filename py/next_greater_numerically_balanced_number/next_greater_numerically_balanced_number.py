'''
Author: fghpdf
Date: 2021-10-24 11:03:13
LastEditTime: 2021-10-24 12:10:24
LastEditors: fghpdf
'''
from typing import List
import unittest
from itertools import permutations

class Solution:

    def convert(self, integers):
      res = int(''.join(map(str, integers)))

      return res

    def nextBeautifulNumber(self, n: int) -> int:
        if n == 0:
          return 1
        
        strNumber = str(n)
        strLen = len(strNumber)
        # 1 - 10
        if strLen == 1:
          return 22

        # 10 - 99:
        if strLen == 2:
          if n <= 22:
            return 22
          else:
            return 122
        
        # 1000 - 9999:
        if strLen >= 3:
           # 1+2, 3:
          comb = []
          comb.extend(set(permutations([1,2,2], 3)))
          comb.extend(set(permutations([3,3,3], 3)))
          comb.sort()
          for c in comb:
            target = self.convert(c)
            if target > n:
              return target
          # 1333, 4444
          comb = []
          comb.extend(set(permutations([1,3,3,3], 4)))
          comb.extend(set(permutations([4,4,4,4], 4)))
          comb.sort()
          for c in comb:
            target = self.convert(c)
            if target > n:
              return target

        # 10000 - 99999:
          # 22333, 14444, 55555
          comb = []
          comb.extend(set(permutations([2,2,3,3,3], 5)))
          comb.extend(set(permutations([1,4,4,4,4], 5)))
          comb.extend(set(permutations([5,5,5,5,5], 5)))
          comb.sort()
          for c in comb:
            target = self.convert(c)
            if target > n:
              return target

        # 10 0000 - 99 9999:
          # 224444, 122333,155555, 666666
          comb = []
          comb.extend(set(permutations([2,2,4,4,4,4], 6)))
          comb.extend(set(permutations([1,2,2,3,3,3], 6)))
          comb.extend(set(permutations([1,5,5,5,5,5], 6)))
          comb.extend(set(permutations([6,6,6,6,6,6], 6)))
          comb.sort()
          for c in comb:
            target = self.convert(c)
            if target > n:
              return target

          # 1+2+4, 1+6, 2+5, 7
          comb = []
          comb.extend(set(permutations([1,2,2,4,4,4,4], 7)))
          comb.extend(set(permutations([1,6,6,6,6,6,6], 7)))
          comb.extend(set(permutations([2,2,5,5,5,5,5], 7)))
          comb.extend(set(permutations([7,7,7,7,7,7,7], 7)))
          comb.sort()
          for c in comb:
            target = self.convert(c)
            if target > n:
              return target

      

        

class TestSolution(unittest.TestCase):
    def testNextBeautifulNumber(self):
        sol = Solution()
        self.assertEqual(sol.nextBeautifulNumber(n=1), 22)
        self.assertEqual(sol.nextBeautifulNumber(n=212), 221)
        self.assertEqual(sol.nextBeautifulNumber(n=23), 122)
        self.assertEqual(sol.nextBeautifulNumber(n = 1000) , 1333)
        self.assertEqual(sol.nextBeautifulNumber(n = 3000), 3133)
        self.assertEqual(sol.nextBeautifulNumber(n = 5000), 14444)

if __name__ == '__main__':
    unittest.main()