'''
Author: fghpdf
Date: 2022-01-01 11:35:48
LastEditTime: 2022-01-01 11:52:11
LastEditors: fghpdf
'''
import unittest
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False

        left = 0
        right = len(s) - 1
        while left < right:
          if s[left] != s[right]:
            return self.validSubstringPalindrome(s, left+1, right) or self.validSubstringPalindrome(s, left, right-1)
          left += 1
          right -= 1
        
        return True

    def validSubstringPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

class TestSolution(unittest.TestCase):
    def testValidPalindrome(self):
        sol = Solution()
        self.assertEqual(sol.validPalindrome("aba"), True)
        self.assertEqual(sol.validPalindrome("abca"), True)
        self.assertEqual(sol.validPalindrome("abc"), False)

if __name__ == '__main__':
    unittest.main()