import unittest
class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
          return 0

        # two stacks
        nums, ops = [], []
        i = 0
        while i < len(s):
          ch = s[i]
          if ch == " ":
            i += 1
            continue
          
          if ch.isdigit():
            num = int(ch)
            while i+1 < len(s) and s[i+1].isdigit():
              num = num * 10 + int(s[i+1])
              i += 1
            nums.append(num)
            i += 1
            continue

          if ch == "(":
            ops.append(ch)
            if (s[i+1] == '-'):
              nums.append(0)
            i += 1
            continue

          if ch == ")":
            # match (
            while ops[-1] != "(":
              nums.append(self.opCalculate(ops.pop(), nums.pop(), nums.pop()))
            ops.pop()
            i += 1
            continue

          if ch in ["+", "-", "*", "/"]:
            while len(ops) > 0 and self.isOpsHighPriority(ch, ops[-1]):
              nums.append(self.opCalculate(ops.pop(), nums.pop(), nums.pop()))
            ops.append(ch)
            i += 1
            continue
        while len(ops) > 0:
            nums.append(self.opCalculate(ops.pop(), nums.pop(), nums.pop()))
        
        return nums.pop()
          

    def opCalculate(self, op: str, second: int, first: int) -> int:
        if op == "+":
          return first + second
        if op == "-":
          return first - second
        if op == "*":
          return first * second
        if op == "/":
          return int(float(first / second))

    # "()" > "*/" > "+-"
    def isOpsHighPriority(self, currentOp: str, opsOp: str) -> bool:
      if opsOp == "(" or opsOp == ")":
        return False
      if (currentOp == "*" or currentOp == "/") \
        and (opsOp == "+" or opsOp == "-"):
        return False
      return True
      

class TestSolution(unittest.TestCase):
    def testCalculate(self):
        sol = Solution()
        self.assertEqual(sol.calculate("1+1"), 2)
        self.assertEqual(sol.calculate("6-4/2"), 4)
        self.assertEqual(sol.calculate("2*(5+5*2)/3+(6/2+8)"), 21)
        self.assertEqual(sol.calculate("(0-3)/4"), 0)

if __name__ == '__main__':
    unittest.main()