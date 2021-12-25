import unittest

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) == 0 or len(num2) == 0:
            return "0"

        maxNum = num1
        if len(num2) > len(num1):
          maxNum = num2

        carry = 0
        res  = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(maxNum)):
            addend1 = 0
            if i < len(num1):
              addend1 = int(num1[i])
            addend2 = 0
            if i < len(num2):
              addend2 = int(num2[i])
            
            sum = addend1 + addend2 + carry
            if sum >= 10:
              carry = 1
            else:
              carry = 0
            
            res.append(sum % 10)

        if carry == 1:
            res.append(1)
        if len(res) == 0:
            return "0"
        res.reverse()
        return "".join(str(v) for v in res)

            

class TestSolution(unittest.TestCase):
    def testAddStrings(self):
        sol = Solution()
        self.assertEqual(sol.addStrings(num1 = "11", num2 = "123"), "134")
        self.assertEqual(sol.addStrings(num1 = "456", num2 = "77"), "533")
        self.assertEqual(sol.addStrings(num1 = "0", num2 = "0"), "0")
        self.assertEqual(sol.addStrings(num1 = "1", num2 = "9"), "10")

if __name__ == "__main__":
    unittest.main()