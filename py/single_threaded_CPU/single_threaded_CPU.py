import heapq
from typing import List
import unittest

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if len(tasks) == 0:
          return []

        res = []
        tasks = sorted([t[0], t[1], i] for i, t in enumerate(tasks))
        i = 0
        h = []
        time = tasks[0][0]
        while len(res) < len(tasks):
          while (i < len(tasks)) and (tasks[i][0] <= time):
            heapq.heappush(h, (tasks[i][1], tasks[i][2]))
            i += 1
          
          if h:
            processTime, originalIndex = heapq.heappop(h)
            time += processTime
            res.append(originalIndex)
          elif i < len(tasks):
            time = tasks[i][0]
        
        return res

class TestSolution(unittest.TestCase):
    def testGetOrder(self):
        sol = Solution()
        self.assertEqual(sol.getOrder([[1,2],[2,4],[3,2],[4,1]]), [0,2,3,1])
        self.assertEqual(sol.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]), [4,3,2,0,1])

if __name__ == '__main__':
    unittest.main()