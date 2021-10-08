'''
Author: fghpdf
Date: 2021-10-08 09:15:14
LastEditTime: 2021-10-08 09:32:22
LastEditors: fghpdf
'''
import unittest

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window 
        window = {}
        # count
        need = {}
        for char in s1:
          need[char] = need.get(char, 0) + 1

        left = 0
        right = 0
        validChar = 0

        while (right < len(s2)):
          # move into window
          char = s2[right]
          right += 1
          # update window
          if len(need) > 0:
            window[char] = window.get(char, 0) + 1
            if window[char] == need.get(char, 0):
              validChar += 1
          
          # shrink
          while (right - left >= len(s1)):
            if validChar == len(need):
              return True
            # remove char from window
            removeChar = s2[left]
            left += 1
            # update window
            if len(need) > 0:
              if window.get(removeChar, 0) == need.get(removeChar, 0):
                validChar -= 1
              window[removeChar] = window.get(removeChar, 0) - 1

        return False


class TestCheckInClusion(unittest.TestCase):
  def test_check_inclusion(self):
    sol = Solution()
    self.assertEqual(sol.checkInclusion("ab", "eidbaooo"), True)
    self.assertEqual(sol.checkInclusion("ab", "eidboaoo"), False)

if __name__ == "__main__":
  unittest.main()