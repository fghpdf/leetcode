'''
Author: fghpdf
Date: 2022-01-09 10:03:23
LastEditTime: 2022-01-09 10:43:51
LastEditors: fghpdf
'''
import unittest

class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 0:
            return s

        res = []
        for c in s:
          if res and res[-1] == c:
              res.pop()
          else:
              res.append(c)

        return ''.join(res)
              

class TestSolution(unittest.TestCase):
    def testRemoveDuplicates(self):
        sol = Solution()
        self.assertEqual(sol.removeDuplicates("aababaab"), "ba")
        self.assertEqual(sol.removeDuplicates(s = "abbaca"), "ca")
        self.assertEqual(sol.removeDuplicates(s = "azxxzy"), "ay")

if __name__ == "__main__":
    unittest.main()
            