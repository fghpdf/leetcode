'''
Author: fghpdf
Date: 2022-02-09 09:01:11
LastEditTime: 2022-02-09 09:24:23
LastEditors: fghpdf
'''
import unittest

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split("\n")
        pathLen = {-1:0}

        res = 0
        for line in lines:
          depth = line.count("\t")
          pathLen[depth] = pathLen[depth-1]+len(line)-depth
          if line.count("."):
            res = max(res, pathLen[depth]+depth)
        return res

class TestSolution(unittest.TestCase):
    def testLengthLongestPath(self):
        sol = Solution()
        self.assertEqual(sol.lengthLongestPath('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext', 20))
        self.assertEqual(sol.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"), 32)
        self.assertEqual(sol.lengthLongestPath("a"), 0)

if __name__ == '__main__':
    unittest.main()