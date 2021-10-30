'''
Author: fghpdf
Date: 2021-10-30 16:01:14
LastEditTime: 2021-10-30 16:28:30
LastEditors: fghpdf
'''
import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s

        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)

        return res

    def helper(self, s: str, low: int, high: int):
        # <- low high ->
        while 0 <= low and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1
        return s[low+1:high]

class TestSolution(unittest.TestCase):
    def testLongestPalindrome(self):
        sol = Solution()
        self.assertEqual(sol.longestPalindrome("babad"), "aba")
        self.assertEqual(sol.longestPalindrome("cbbd"), "bb")
        self.assertEqual(sol.longestPalindrome("a"), "a")
        self.assertEqual(sol.longestPalindrome("ac"), "c")

if __name__ == "__main__":
    unittest.main()