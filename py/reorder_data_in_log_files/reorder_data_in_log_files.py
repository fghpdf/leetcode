'''
Author: fghpdf
Date: 2022-01-25 09:11:33
LastEditTime: 2022-01-25 09:19:19
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs) == 0:
          return []
        
        digits = []
        letters = []
        for log in logs:
          if log.split()[1].isdigit():
            digits.append(log)
          else:
            letters.append(log)
        
        letters.sort(key = lambda letter: letter.split()[0])
        letters.sort(key = lambda letter: letter.split()[1:])

        res = letters + digits
        return res

class TestSolution(unittest.TestCase):
    def testReorderLogFiles(self):
        sol = Solution()
        self.assertEqual(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]), ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])
        self.assertEqual(sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]), ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])

if __name__ == '__main__':
    unittest.main()