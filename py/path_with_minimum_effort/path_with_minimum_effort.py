from typing import List
import unittest

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if len(heights) == 0:
          return 0

        def canReachDestination(threadshold):
            self.visited = set()
            return self.helper(heights, 0, 0, threadshold)

        left = 0
        ans = right = 10**6
        while left <= right:
            mid = left + (right-left)//2
            if canReachDestination(mid):
                right = mid - 1 # Try to find better result on the left side
                ans = mid
            else:
                left = mid + 1
        return ans

    def helper(self, heights: List[List[int]], row: int, col: int, threadshold: int) -> bool:
        if row == len(heights)-1 and col == len(heights[row])-1:
          return True
        self.visited.add((row, col))
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dir in dirs:
          newRow, newCol = row+dir[0], col+dir[1]
          if 0 <= newRow < len(heights) and 0 <= newCol < len(heights[row]) and (newRow, newCol) not in self.visited:
            if abs(heights[row][col]-heights[newRow][newCol]) <= threadshold and self.helper(heights, newRow, newCol, threadshold):
              return True
        
        return False

class TestSolution(unittest.TestCase):
    def testMinimumEffortPath(self):
        sol = Solution()
        self.assertEqual(sol.minimumEffortPath([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]), 5)
        self.assertEqual(sol.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]), 2)
        self.assertEqual(sol.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]), 1)
        self.assertEqual(sol.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]), 0)
        

if __name__ == '__main__':
    unittest.main()