from typing import List
import unittest

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len(expression) == 0:
            return []

        m = {}
        return self.dfs(expression, m)

    def dfs(self, expression: str, m) -> List[int]:
        if expression in m:
            return m[expression]
        if expression.isdigit():
            m[expression] = int(expression)
            return [int(expression)]
        res = []
        for i, ch in enumerate(expression):
            if ch in '+-*':
                l = self.diffWaysToCompute(expression[:i])
                r = self.diffWaysToCompute(expression[i+1:])
                res.extend(eval(str(x)+ch+str(y)) for x in l for y in r)
        m[expression] = res
        return res

class TestSolution(unittest.TestCase):
    def testDiffWaysToCompute(self):
        sol = Solution()
        self.assertEqual(sol.diffWaysToCompute("2-1-1"), [2,0])
        self.assertEqual(sol.diffWaysToCompute("2*3-4*5"), [-34,-10,-14,-10,10])

if __name__ == '__main__':
    unittest.main()