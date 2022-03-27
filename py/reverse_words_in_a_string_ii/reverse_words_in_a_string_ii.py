from typing import List
import unittest

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.swap(s, 0, len(s)-1)

        # reverse word
        wordStart = 0
        for i in range(len(s)):
          if s[i] == " ":
            self.swap(s, wordStart, i-1)
            wordStart = i+1
          elif len(s)-1 == i:
            self.swap(s, wordStart, i)

    def swap(self, s, start, end) -> None:
      while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
        

class TestSolution(unittest.TestCase):
    def testReverseWords(self):
        sol = Solution()
        s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        sol.reverseWords(s)
        self.assertEqual(s, ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"])
        s = ["a"]
        sol.reverseWords(s)
        self.assertEqual(s, ["a"])

if __name__ == '__main__':
    unittest.main()