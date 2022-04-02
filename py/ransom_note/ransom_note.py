from typing import Counter
import unittest

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0:
          return True

        c = Counter(ransomNote)
        for letter in magazine:
          if letter in c:
            c[letter] -= 1
        
        for key in c:
          if c[key] > 0:
            return False

        return True

class TestSolution(unittest.TestCase):
    def testCanConstruct(self):
        sol = Solution()
        self.assertEqual(sol.canConstruct(ransomNote = "a", magazine = "b"), False)
        self.assertEqual(sol.canConstruct(ransomNote = "aa", magazine = "ab"), False)
        self.assertEqual(sol.canConstruct(ransomNote = "aa", magazine = "aab"), True)

if __name__ == '__main__':
    unittest.main()