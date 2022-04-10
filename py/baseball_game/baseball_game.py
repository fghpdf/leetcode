from typing import List
import unittest

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if len(ops) == 0:
          return 0

        scores = []
        for op in ops:
          if op.lstrip("-").isdigit():
            scores.append(int(op))
          # stack pop
          if op == "C":
            scores.pop()
          # double stack top
          if op == "D":
            scores.append(2*scores[-1])
          if op == "+":
            scores.append(scores[-1]+scores[-2])
        return sum(scores)

class TestSolution(unittest.TestCase):
    def testCalPoints(self):
      sol = Solution()
      self.assertEqual(sol.calPoints(["5","2","C","D","+"]), 30)
      self.assertEqual(sol.calPoints(["5","-2","4","C","D","9","+","+"]), 27)

if __name__ == '__main__':
    unittest.main()