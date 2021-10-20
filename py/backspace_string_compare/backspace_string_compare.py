'''
Author: fghpdf
Date: 2021-10-20 09:21:59
LastEditTime: 2021-10-20 09:35:22
LastEditors: fghpdf
'''
import unittest

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        for c in s:
          if c.isalpha():
            sStack.append(c)
          if c == '#' and sStack:
            sStack.pop()

        tStack = []
        for c in t:
          if c.isalpha():
            tStack.append(c)
          if c == '#' and tStack:
            tStack.pop()

        return sStack == tStack

class TestSolution(unittest.TestCase):
    def testBackspaceCompare(self):
        sol = Solution()
        self.assertEqual(sol.backspaceCompare("ab#c", "ad#c"), True)
        self.assertEqual(sol.backspaceCompare(s = "ab##", t = "c#d#"), True)
        self.assertEqual(sol.backspaceCompare( s = "a##c", t = "#a#c"), True)
        self.assertEqual(sol.backspaceCompare(s = "a#c", t = "b"), False)

if __name__ == '__main__':
    unittest.main()