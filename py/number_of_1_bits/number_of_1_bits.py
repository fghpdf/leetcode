'''
Author: fghpdf
Date: 2021-10-15 09:45:34
LastEditTime: 2021-10-15 09:54:13
LastEditors: fghpdf
'''
import unittest

class Solution:
    def hammingWeight(self, n: int) -> int:
      if n == 0:
        return n  
      
      count = 0
      while n:
        n &= n - 1
        count += 1

      return count

class TestHammingWeight(unittest.TestCase):
    def test_hamming_weight(self):
      sol = Solution()
      self.assertEqual(sol.hammingWeight('00000000000000000000000000001011'), 3)
      self.assertEqual(sol.hammingWeight(int('00000000000000000000000010000000')), 1)
      self.assertEqual(sol.hammingWeight(int('11111111111111111111111111111101')), 31)
      

if __name__ == '__main__':
    unittest.main()
