import unittest

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1

        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product

        return ans
class TestSolution(unittest.TestCase):
    def testCountNumbersWithUniqueDigits(self):
        sol = Solution()
        self.assertEqual(sol.countNumbersWithUniqueDigits(2), 91)
        self.assertEqual(sol.countNumbersWithUniqueDigits(0), 1)

if __name__ == '__main__':
    unittest.main()