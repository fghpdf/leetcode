import unittest

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == 0 or len(str2) == 0:
            return str1 if str1 else str2
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)

        if str1[:len(str2)] == str2:
           return self.gcdOfStrings(str1[len(str2):], str2)

        return ""

        

class TestSolution(unittest.TestCase):
    def testGcdOfStrings(self):
        sol = Solution()
        self.assertEqual(sol.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"), "ABC")
        self.assertEqual(sol.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"), "AB")
        self.assertEqual(sol.gcdOfStrings(str1 = "LEET", str2 = "CODE"), "")
        self.assertEqual(sol.gcdOfStrings(str1 = "ABCDEF", str2 = "ABC"), "")

if __name__ == '__main__':
    unittest.main()