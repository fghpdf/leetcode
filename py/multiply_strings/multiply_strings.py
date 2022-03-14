from collections import defaultdict
import unittest

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 0 or len(num2) == 0:
          return "0"

        baseNum = num1
        mulNum = num2
        if len(num2) > len(num1):
          baseNum = num2
          mulNum = num1

        res = [0] * (len(num1) + len(num2))
        for i in range(len(mulNum)-1, -1, -1):
          for j in range(len(baseNum)-1, -1, -1):
            p1 = i + j
            p2 = i + j + 1
            sum = int(mulNum[i])*int(baseNum[j])+res[p2]

            res[p1] += sum // 10
            res[p2] = sum % 10

        cut = 0
        for i in range(len(res[cut:])):
          if res[i] != 0:
            break
          cut = i + 1

        if len(res) == 0:
          return "0"

        return "".join([str(x) for x in res[cut:]])        
            

class TestSolution(unittest.TestCase):
    def testMultiply(self):
      sol = Solution()
      self.assertEqual(sol.multiply(num1 = "2", num2 = "3"), "6")
      self.assertEqual(sol.multiply(num1 = "123", num2 = "456"), "56088")

if __name__ == "__main__":
    unittest.main()