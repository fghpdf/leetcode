import unittest

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(word) == 0:
            return False

        i, j = 0, 0
        digit = 0
        while i < len(word) and j < len(abbr):
            if digit == 0 and abbr[j] == "0":
              return False

            if not abbr[j].isdigit():
                digit = 0
                if abbr[j] == word[i]:
                  i += 1
                  j += 1
                else:
                  return False
            else:
              while j < len(abbr) and abbr[j].isdigit():
                  digit = digit * 10 + int(abbr[j])
                  j += 1
              i += digit

        return i == len(word) and j == len(abbr)

class TestSolution(unittest.TestCase):
    def testValidWordAbbreviation(self):
        sol = Solution()
        self.assertEqual(sol.validWordAbbreviation(word = "internationalization", abbr = "i12iz4n"), True)
        self.assertEqual(sol.validWordAbbreviation(word = "apple", abbr = "a2e"), False)

if __name__ == '__main__':
    unittest.main()