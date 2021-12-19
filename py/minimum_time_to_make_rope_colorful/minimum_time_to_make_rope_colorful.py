from typing import List
import unittest

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = maxCost = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                maxCost = 0

            res += min(maxCost, neededTime[i])
            maxCost = max(maxCost, neededTime[i])

        return res

class TestSolution(unittest.TestCase):
    def testMinCost(self):
        sol = Solution()
        self.assertEqual(sol.minCost(colors = "abaac", neededTime = [1,2,3,4,5]), 3)
        self.assertEqual(sol.minCost(colors = "abc", neededTime = [1,2,3]), 0)
        self.assertEqual(sol.minCost(colors = "aabaa", neededTime = [1,2,3,4,1]), 2)

if __name__ == '__main__':
    unittest.main()