'''
Author: fghpdf
Date: 2022-01-16 19:31:18
LastEditTime: 2022-01-16 19:52:57
LastEditors: fghpdf
'''
import unittest

class Solution:
    def intToRoman(self, num: int) -> str:
        thousand = num // 1000
        hundred = num // 100 % 10
        ten = num // 10 % 10
        single = num // 1 % 10

        res = ""
        if thousand > 0:
          res += thousand * "M"

        if hundred > 0 and hundred <= 3:
          res += hundred * "C"
        elif hundred == 4:
          res += "CD"
        elif hundred > 4 and hundred < 9:
          res += ("D" + (hundred-5)*"C")
        elif hundred == 9:
          res += "CM"
        
        if ten > 0 and ten <= 3:
          res += ten * "X"
        elif ten == 4:
          res += "XL"
        elif ten > 4 and ten < 9:
          res += ("L"+(ten-5)*"X")
        elif ten == 9:
          res += "XC"

        if single > 0 and single <= 3:
          res += single * "I"
        elif single == 4:
          res += "IV"
        elif single > 4 and single < 9:
          res += ("V"+(single-5)*"I")
        elif single == 9:
          res += "IX"
      
        return res
        

class TestSolution(unittest.TestCase):
    def testIntToRoman(self):
        sol = Solution()
        self.assertEqual(sol.intToRoman(3), "III")
        self.assertEqual(sol.intToRoman(58), "LVIII")
        self.assertEqual(sol.intToRoman(1994), "MCMXCIV")

if __name__ == "__main__":
    unittest.main()