'''
Author: fghpdf
Date: 2022-02-10 08:53:45
LastEditTime: 2022-02-10 09:19:41
LastEditors: fghpdf
'''
import unittest

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ''

        for c in s:
          if c.isdigit():
            curNum = curNum*10+int(c)
            continue
          
          if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
            continue

          if c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num*curString
            continue

          curString += c
        
        return curString

class TestSolution(unittest.TestCase):
    def testDecodeString(self):
        sol = Solution()
        self.assertEqual(sol.decodeString(s = "3[a]2[bc]"), "aaabcbc")
        self.assertEqual(sol.decodeString(s = "3[a2[c]]"), "accaccacc")
        self.assertEqual(sol.decodeString(s = "2[abc]3[cd]ef"), "abcabccdcdcdef")

if __name__ == "__main__":
    unittest.main()
