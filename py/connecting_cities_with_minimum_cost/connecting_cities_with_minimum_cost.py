'''
Author: fghpdf
Date: 2022-01-24 09:08:43
LastEditTime: 2022-01-24 09:21:42
LastEditors: fghpdf
'''
import collections
import heapq
from typing import List
import unittest

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) == 0:
            return 0
        
        coll = collections.defaultdict(list)
        for cityA, cityB, cost in connections:
            coll[cityA].append((cost, cityB))
            coll[cityB].append((cost, cityA))
        
        queue = [(0,n)]
        visited = set()
        total = 0
        while queue and len(visited) < n:
          cost, city = heapq.heappop(queue)
          if city not in visited:
            visited.add(city)
            total += cost
            for edge_cost, next_city in coll[city]:
                heapq.heappush(queue, (edge_cost, next_city))
        
        return total if len(visited) == n else -1

class TestSolution(unittest.TestCase):
    def testMinimumCost(self):
        sol = Solution()
        self.assertEqual(sol.minimumCost(n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]), 6)
        self.assertEqual(sol.minimumCost(n = 4, connections = [[1,2,3],[3,4,4]]), -1)

if __name__ == "__main__":
    unittest.main()