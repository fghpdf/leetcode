from typing import List
import unittest

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        if len(dict) == 0:
          return False

        seen = set()
        for word in dict:
          for i, c in enumerate(word):
            # "abcd" -> ".bcd" or "a.cd" and so on
            masked_word = word[:i] + '.' + word[i+1:]
            if masked_word in seen:
              return True
            else:
              seen.add(masked_word)
        return False

class TestSolution(unittest.TestCase):
    def testDifferByOne(self):
        sol = Solution()
        self.assertEqual(sol.differByOne(["abcd","acbd", "aacd"]), True)
        self.assertEqual(sol.differByOne(["ab","cd","yz"]), False)
        self.assertEqual(sol.differByOne(["abcd","cccc","abyd","abab"]), True)

if __name__ == '__main__':
    unittest.main()