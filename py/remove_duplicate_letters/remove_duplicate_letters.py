from typing import Counter
import unittest

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 0:
          return s

        lastIndex = {}
        for i in range(len(s)):
          lastIndex[s[i]] = i

        res = []
        visited = set()

        for i in range(len(s)):
          if s[i] not in visited:
            while (res and res[-1] > s[i] and lastIndex[res[-1]] > i):
              visited.remove(res.pop())

            visited.add(s[i])
            res.append(s[i])

        return "".join(res)

class TestSolution(unittest.TestCase):
    def testRemoveDuplicateLetters(self):
        sol = Solution()
        self.assertEqual(sol.removeDuplicateLetters(s = "bcabc"), "abc")
        self.assertEqual(sol.removeDuplicateLetters(s = "cbacdcbc"), "acdb")

if __name__ == "__main__":
    unittest.main()