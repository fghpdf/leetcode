from typing import List
import unittest

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        candidates.sort()
        res = []
        track = []
        self.backtrack(candidates, track, target, res, 0)
        return res

    def backtrack(self, candidates: List[int], track: List[int],remain: int, res: List[List[int]], start):
        if remain < 0:
            return

        if remain == 0:
            res.append(track[:])
            return
        
        for i in range(start, len(candidates)):
          if start == i or candidates[i] != candidates[i-1]:
            track.append(candidates[i])
            self.backtrack(candidates, track, remain-candidates[i], res, i+1)
            track.pop()

class TestSolution(unittest.TestCase):
    def testCombinationSum2(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8), [[1,1,6],[1,2,5],[1,7],[2,6]])
        self.assertEqual(sol.combinationSum2(candidates = [2,5,2,1,2], target = 5), [[1,2,2],[5]])

if __name__ == '__main__':
    unittest.main()