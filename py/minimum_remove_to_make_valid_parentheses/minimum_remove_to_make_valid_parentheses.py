'''
Author: fghpdf
Date: 2022-01-10 09:01:18
LastEditTime: 2022-01-10 09:20:22
LastEditors: fghpdf
'''
import unittest

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 0:
            return s

        parenthesesStack = []
        needRemoveDict = {}
        for i, c in enumerate(s):
            if c == "(":
              parenthesesStack.append((i,c))
            if c == ")":
              if len(parenthesesStack) > 0 and parenthesesStack[-1][1] == "(":
                  parenthesesStack.pop()
              else:
                  needRemoveDict[i] = c

        for p in parenthesesStack:
            needRemoveDict[p[0]] = p[1]
        res = []
        for i, c in enumerate(s):
            if i not in needRemoveDict:
                res.append(c)

        return "".join(res)


class TestSolution(unittest.TestCase):
    def testMinRemoveToMakeValid(self):
        sol = Solution()
        self.assertEqual(sol.minRemoveToMakeValid(s = "lee(t(c)o)de)"), "lee(t(c)o)de")
        self.assertEqual(sol.minRemoveToMakeValid(s = "a)b(c)d"), "ab(c)d")
        self.assertEqual(sol.minRemoveToMakeValid(s = "))(("), "")

if __name__ == "__main__":
    unittest.main()        