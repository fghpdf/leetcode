'''
Author: fghpdf
Date: 2022-02-14 08:29:19
LastEditTime: 2022-02-14 08:56:07
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1==p2==p3==p4:return False
        def dist(x,y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        ls=[dist(p1,p2),dist(p1,p3),dist(p1,p4),dist(p2,p3),dist(p2,p4),dist(p3,p4)]
        ls.sort()
        if ls[0]==ls[1]==ls[2]==ls[3]:
            if ls[4]==ls[5]:
                return True
        return False

class TestSolution(unittest.TestCase):
    def testValidSquare(self):
        sol = Solution()
        self.assertEqual(sol.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]), True)
        self.assertEqual(sol.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]), False)
        self.assertEqual(sol.validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]), True)
        self.assertEqual(sol.validSquare(p1=[0,0],p2=[0,0],p3=[0,0],p4=[0,0]), False)

if __name__ == '__main__':
    unittest.main()