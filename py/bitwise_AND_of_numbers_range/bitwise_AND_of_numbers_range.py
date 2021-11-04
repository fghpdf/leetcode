import unittest

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return right << i

class TestSolution(unittest.TestCase):
    def testRangeBitwiseAnd(self):
        sol = Solution()
        self.assertEqual(sol.rangeBitwiseAnd(left = 5, right = 7), 4)
        self.assertEqual(sol.rangeBitwiseAnd(left = 0, right = 0), 0)
        self.assertEqual(sol.rangeBitwiseAnd(left = 1, right = 2147483647), 0)

if __name__ == '__main__':
    unittest.main()