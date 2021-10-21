from typing import List
import unittest


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      need = {}
      window = {}

      # init
      for c in p:
        need[c] = need.get(c, 0) + 1
        window[c] = 0

      left = 0
      right = 0
      # need times == times in window
      times = 0

      result = []
      while right < len(s):
        moveInChar = s[right]
        right += 1

        # judge valid and update window
        if moveInChar in need:
          window[moveInChar] += 1
          if window.get(moveInChar) == need.get(moveInChar):
            times += 1

        while right - left >= len(p):
          moveOutChar = s[left]
          if times == len(need):
            result.append(left)

          left += 1

          # move out
          if moveOutChar in need:
            if window.get(moveOutChar) == need.get(moveOutChar):
              times -= 1
            
            window[moveOutChar] -= 1
      
      return result

class TestSolution(unittest.TestCase):
    def testFindAnagrams(self):
      sol = Solution()
      self.assertEqual(sol.findAnagrams(s = "cbaebabacd", p = "abc"), [0,6])
      self.assertEqual(sol.findAnagrams(s = "abab", p = "ab"), [0,1,2])

if __name__ == '__main__':
    unittest.main()