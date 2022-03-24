import unittest
 
# the rule is
# A: 26 ^ 0 * 1
# AA: 26 ^ 1 * 1 + 26 ^ 0 * 1 = 27
# AAA: 26 ^ 2 * 1 + 26 * 1 + 1 = 703
 
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
          return ""

        return self.convertToTitle((columnNumber-1)//26) + chr((columnNumber - 1) % 26 + ord("A"))

        
class TestSolution(unittest.TestCase):
    def testConvertToTitle(self):
        sol = Solution()
        self.assertEqual(sol.convertToTitle(1), "A")
        self.assertEqual(sol.convertToTitle(28), "AB")
        self.assertEqual(sol.convertToTitle(701), "ZY")

if __name__ == '__main__':
    unittest.main()