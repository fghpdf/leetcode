'''
Author: fghpdf
Date: 2022-02-03 09:09:39
LastEditTime: 2022-02-03 09:24:08
LastEditors: fghpdf
'''
from math import sqrt
import unittest

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1,n+1):
          if n % i == 0:
            res.append(i)

        if k > len(res):
            return -1
        res.sort()
        return res[k-1]

    def kthFactor2(self, n, k):
        f1, f2 = [], []
        for s in range(1, int(sqrt(n)) + 1 ):
            if n % s == 0:
                f1 += [s]
                f2 += [n//s]
                
        if f1[-1] == f2[-1]: f2.pop()
            
        factors = f1 + f2[::-1]
        return -1 if len(factors) < k else factors[k-1]

class TestSolution(unittest.TestCase):
    def testKthFactor(self):
        sol = Solution()
        self.assertEqual(sol.kthFactor(12,3), 3)
        self.assertEqual(sol.kthFactor(7,2), 7)
        self.assertEqual(sol.kthFactor(4,4), -1)

if __name__ == '__main__':
    unittest.main()