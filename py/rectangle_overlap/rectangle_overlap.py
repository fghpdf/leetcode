from typing import List
import unittest

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if len(rec1) == 0 or len(rec2) == 0:
            return False

        # rec1.x2 > rec2.x1 and rec2.x2 > rec.x1 and rec1.y2 > rec2.y1 and rec2.y2 > rec1.y1
        if rec1[2] > rec2[0] and \
          rec2[2] > rec1[0] and \
            rec1[3] > rec2[1] and \
              rec2[3] > rec1[1]:
              return True
        
        return False


class TestSolution(unittest.TestCase):
    def testIsRectangleOverlap(self):
        sol = Solution()
        self.assertEqual(sol.isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]), True)
        self.assertEqual(sol.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]),  False)
        self.assertEqual(sol.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]), False)

if __name__ == '__main__':
    unittest.main()