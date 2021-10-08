'''
Author: fghpdf
Date: 2021-10-08 08:52:56
LastEditTime: 2021-10-08 09:05:52
LastEditors: fghpdf
'''
import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
          return 0
        # window char -> count
        window = {}

        left = 0
        right = 0
        res = 0

        while (right < len(s)):
          char = s[right]
          right += 1
          # update window
          window[char] = window.get(char, 0) + 1
          # judge whether left window needs shrink
          # repeat chars
          while (window[char] > 1):
            removeChar = s[left]
            left += 1
            # update window
            window[removeChar] = window.get(removeChar, 0) - 1
          
          # update res
          res = max(res, right - left)

        return res

class TestLengthOfLongestSubString(unittest.TestCase):
  def test_length_of_longest_sub_string(self):
    sol = Solution()
    self.assertEqual(sol.lengthOfLongestSubstring("abcabcbb"), 3)
    self.assertEqual(sol.lengthOfLongestSubstring("bbbbb"), 1)
    self.assertEqual(sol.lengthOfLongestSubstring(""), 0)


if __name__ == "__main__":
  unittest.main()