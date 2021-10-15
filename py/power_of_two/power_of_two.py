'''
Author: fghpdf
Date: 2021-10-15 09:30:08
LastEditTime: 2021-10-15 09:34:31
LastEditors: fghpdf
'''
import unittest

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
          return False

        while n % 2 == 0:
          n = n // 2

        return n == 1

class TestIsPowerOfTwo(unittest.TestCase):
    def test_is_power_of_two(self):
        sol = Solution()
        self.assertEqual(sol.isPowerOfTwo(1), True)
        self.assertEqual(sol.isPowerOfTwo(16), True)
        self.assertEqual(sol.isPowerOfTwo(3), False)
        self.assertEqual(sol.isPowerOfTwo(5), False)

if __name__ == '__main__':
    unittest.main()