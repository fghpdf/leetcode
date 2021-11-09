from typing import List
import unittest

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if len(customers) == 0:
            return 0

        newCustomers = sorted(customers, key=lambda d: d[0])
        res = 0
        lastEnd = 0
        for c in newCustomers:
          start = c[0]
          need = c[1]

          if lastEnd != 0 and start >= lastEnd:
            res += need
            lastEnd = start+need
          elif lastEnd != 0 and start < lastEnd:
            res += lastEnd + need - start
            lastEnd += need
          elif lastEnd == 0:
            res += need
            lastEnd = start+need

        return res/len(customers)

class TestSolution(unittest.TestCase):
    def testAverageWaitingTime(self):
        sol = Solution()
        self.assertEqual(sol.averageWaitingTime([[1,2],[2,5],[4,3]]), 5.00000)
        self.assertEqual(sol.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]), 3.25000)

if __name__ == '__main__':
    unittest.main()