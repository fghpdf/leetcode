'''
Author: fghpdf
Date: 2022-01-03 10:30:26
LastEditTime: 2022-01-03 10:53:24
LastEditors: fghpdf
'''
import unittest
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if len(s) == 0 or len(order) == 0:
            return ""

        charMemo = {}
        for c in s:
          charMemo[c] = charMemo.get(c, 0) + 1
        
        print(charMemo)
        res = []
        for c in order:
          if c in charMemo:
            while charMemo[c] != 0:
              res.append(c)
              charMemo[c] -= 1

        for k, v in charMemo.items():
            if v != 0:
              res.extend(k*v)

        return ''.join(res)

class TestSolution(unittest.TestCase):
    def testCustomSortString(self):
        sol = Solution()
        self.assertEqual(sol.customSortString(order = "cba", s = "abcd"), "cbad")
        self.assertEqual(sol.customSortString(order = "cbafg", s = "abcd"), "cbad")
        self.assertEqual(sol.customSortString(order="hucw", s="utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"), 
"hhhhhuucccwaaaaaaaaabbdddddeffffggggiijjjjkkkkllllmmmmnnnoooopppqqqqqqqqqqqrsssttttttttvxxxxxyyzzzzz")

if __name__ == '__main__':
    unittest.main()