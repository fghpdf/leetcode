'''
Author: fghpdf
Date: 2021-10-06 08:53:13
LastEditTime: 2021-10-06 08:57:11
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # too slow
        # s.reverse()

        # two pointer
        left = 0
        right = len(s) - 1
        while left < right:
          temp = s[left]
          s[left] = s[right]
          s[right] = temp
          left+=1
          right-=1


class TestReverseString(unittest.TestCase):
  def test_reverse_string(self):
    sol = Solution()
    s = ["h","e","l","l","o"]
    sol.reverseString(s)
    self.assertEqual(s, ["o","l","l","e","h"])


if __name__ == "__main__":
  unittest.main()