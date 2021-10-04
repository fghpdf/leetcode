import unittest

from search_insert_position import Solution

class TestSearchInsertPosition(unittest.TestCase):
    def test_search_insert_postion(self):
      sol = Solution()
      self.assertEqual(sol.searchInsert([1, 2, 3, 4, 5], 3), 2)
      self.assertEqual(sol.searchInsert([1, 2, 3, 4, 5], 6), 5)
      self.assertEqual(sol.searchInsert([1, 3, 5, 6], 5), 2)
      self.assertEqual(sol.searchInsert([1, 3, 5, 6], 2), 1)
      self.assertEqual(sol.searchInsert([1, 3, 5, 6], 0), 0)
      self.assertEqual(sol.searchInsert([1], 0), 0)



if __name__ == '__main__':
    unittest.main()