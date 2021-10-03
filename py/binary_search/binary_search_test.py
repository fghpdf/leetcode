import unittest

from binary_search import Solution

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        sol = Solution()
        self.assertEqual(sol.search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(sol.search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(sol.search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(sol.search([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(sol.search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(sol.search([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(sol.search([1, 2, 3, 4, 5], 4), 3)

if __name__ == '__main__':
    unittest.main()