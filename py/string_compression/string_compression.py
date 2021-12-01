from typing import List
import unittest

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0

        indexAns = 0
        lenChars = len(chars)
        index = 0
        while index < lenChars:
          currentChar = chars[index]

          count = 0
          while index < lenChars and chars[index] == currentChar:
            count += 1
            index += 1
          
          chars[indexAns] = currentChar
          indexAns += 1

          if count != 1:
              for c in str(count):
                chars[indexAns] = c
                indexAns += 1
        chars[:] = chars[:indexAns]
        return indexAns

class TestSolution(unittest.TestCase):
    def testCompress(self):
        sol = Solution()
        chars = ["a","a","b","b","c","c","c"]
        self.assertEqual(sol.compress(chars), 6)
        self.assertEqual(chars, ["a","2","b","2","c","3"])
        chars = ["a"]
        self.assertEqual(sol.compress(chars), 1)
        self.assertEqual(chars, ["a"])
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        self.assertEqual(sol.compress(chars), 4)
        self.assertEqual(chars, ["a","b","1","2"])
        chars = ["a","a","a","b","b","a","a"]
        self.assertEqual(sol.compress(chars), 6)
        self.assertEqual(chars, ["a","3","b","2","a","2"])

if __name__ == '__main__':
    unittest.main()