'''
Author: fghpdf
Date: 2021-12-31 09:10:23
LastEditTime: 2021-12-31 09:26:52
LastEditors: fghpdf
'''
import unittest
class Solution:
    def maximumSwap(self, num: int) -> int:
        numList = [int(x) for x in str(num)]
        last = {x:i for i, x in enumerate(numList)}
        for i, x in enumerate(numList):
          for right in range(9,x,-1):
            if right in last:
                rightIndex = last[right]
                if rightIndex > i:
                  # swap
                  temp = numList[rightIndex]
                  numList[rightIndex] = numList[i]
                  numList[i] = temp
                  return int(''.join(map(str,numList)))
        return num

class TestSolution(unittest.TestCase):
    def testMaximumSwap(self):
        sol = Solution()
        self.assertEqual(sol.maximumSwap(2736), 7236)
        self.assertEqual(sol.maximumSwap(9973), 9973)


if __name__ == "__main__":
    unittest.main()