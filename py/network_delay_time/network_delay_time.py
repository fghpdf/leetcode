from typing import List
import unittest
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) == 0:
            return -1
        
        dic={i:[] for i in range(1,n+1)}
        for s,e,w in times:
            dic[s].append((w,e))
        heap=[(0,k)]
        visited=set()
        self.ans=0
        def bfs(heap):
            while heap:
                # heapq.heapify(heap)
                w,node=heapq.heappop(heap)
                if node in visited:
                    continue
                self.ans=max(self.ans,w)
                visited.add(node)
                for wei,nei in dic[node]:
                    heapq.heappush(heap,(wei+w,nei))     
            return self.ans if len(visited)==n else -1
        return bfs(heap)

class TestSolution(unittest.TestCase):
    def testNetworkDelayTime(self):
        sol = Solution()
        self.assertEqual(sol.networkDelayTime( times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2), 2)
        self.assertEqual(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 1), 1)
        self.assertEqual(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2), -1)

if __name__ == '__main__':
    unittest.main()