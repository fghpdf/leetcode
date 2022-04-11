from typing import List
import unittest

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if len(grid) == 0:
          return []

        if k == 0:
          return grid

        grid1 = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
          for j in range(len(grid[i])):
            if j == len(grid[i])-1 and i < len(grid)-1:
              grid1[i+1][0] = grid[i][j]
            elif j < len(grid[i]) -1:
              grid1[i][j+1] = grid[i][j]
        
        grid1[0][0] = grid[-1][-1]
        k -= 1
        return self.shiftGrid(grid1, k)

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col, nums = len(grid[0]), sum(grid, [])
        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]
        return [nums[i:i+col] for i in range(0, len(nums), col)]
        

class TestSolution(unittest.TestCase):
    def testShiftGrid(self):
        sol = Solution()
        self.assertEqual(sol.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1), [[9,1,2],[3,4,5],[6,7,8]])
        self.assertEqual(sol.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4), [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]])
        self.assertEqual(sol.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9), [[1,2,3],[4,5,6],[7,8,9]])

if __name__ == '__main__':
    unittest.main()