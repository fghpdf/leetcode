from typing import List
import unittest

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0

        result = []
        while i < len(firstList) and j < len(secondList):
            firstStart, firstEnd = firstList[i]
            secondStart, secondEnd = secondList[j]

            if firstStart <= secondEnd and secondStart <= firstEnd: # lock
                result.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])

            if firstEnd <= secondEnd:
                i += 1
            else:
                j += 1
        return result

class TestSolution(unittest.TestCase):
    def testIntervalIntersection(self):
        sol = Solution()
        self.assertEqual(sol.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]), [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
        self.assertEqual(sol.intervalIntersection(firstList = [[1,3],[5,9]], secondList = []), [])
        self.assertEqual(sol.intervalIntersection(firstList = [], secondList = [[4,8],[10,12]]), [])
        self.assertEqual(sol.intervalIntersection(firstList = [[1,7]], secondList = [[3,10]]), [[3,7]])

if __name__ == '__main__':
    unittest.main()