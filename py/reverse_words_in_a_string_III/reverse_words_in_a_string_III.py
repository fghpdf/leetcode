'''
Author: fghpdf
Date: 2021-10-06 09:06:33
LastEditTime: 2021-10-06 09:20:00
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def reverseWords(self, s: str) -> str:
        splitStrings = s.split(" ")
        for index in range(len(splitStrings)):
          splitStr = splitStrings[index]
          splitStrings[index] = splitStr[::-1]

        return " ".join(splitStrings)


class TestReverseWords(unittest.TestCase):
  def test_reverse_words(self):
    sol = Solution()
    self.assertEqual(sol.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")
    self.assertEqual(sol.reverseWords("God Ding"), "doG gniD")


if __name__ == '__main__':
  unittest.main()