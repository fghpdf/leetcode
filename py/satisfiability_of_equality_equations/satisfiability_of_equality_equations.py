import string
from typing import List
import unittest

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        if len(equations) == 0:
          return False

        def find(x):
          if x != uf[x]: 
            uf[x] = find(uf[x])
          return uf[x]

        uf = {a: a for a in string.ascii_lowercase}
        for a, e, _, b in equations:
          if e == "=":
            uf[find(a)] = find(b)
        
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)

class TestSolution(unittest.TestCase):
    def testEquationsPossible(self):
        sol = Solution()
        self.assertEqual(sol.equationsPossible(["a==b","b!=a"]), False)
        self.assertEqual(sol.equationsPossible(["b==a","a==b"]), True)

if __name__ == '__main__':
    unittest.main()