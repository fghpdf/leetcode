import heapq
from typing import List
import unittest

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones or len(stones) == 0:
          return 0

        if len(stones) == 1:
          return stones[0]

        stones.sort(reverse=True)

        x = stones[0]
        y = stones[1]

        newStones = stones[2:]
        newStones.append(abs(x-y))

        return self.lastStoneWeight(newStones)

class OnlognSolution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]
                

class TestSolution(unittest.TestCase):
    def testLastStoneWeight(self):
        sol = Solution()
        self.assertEqual(sol.lastStoneWeight(stones = [2,7,4,1,8,1]), 1)
        self.assertEqual(sol.lastStoneWeight(stones = [1]), 1)

if __name__ == '__main__':
    unittest.main()