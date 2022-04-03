from typing import List
import unittest

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gates = []
        for row in range(len(rooms)):
          for col in range(len(rooms[row])):
            if rooms[row][col] == 0:
              gates.append((row, col))
        for row, col in gates:
          for i, j in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
            if i >= 0 and i < len(rooms) and \
              j >= 0 and j < len(rooms[i]) and \
                rooms[i][j] > 2**30:
                rooms[i][j] = rooms[row][col] + 1
                gates.append((i, j))    

class TestSolution(unittest.TestCase):
    def testWallsAndGates(self):
        sol = Solution()
        rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
        sol.wallsAndGates(rooms)
        self.assertEqual(rooms, [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]])
        rooms = [[-1]]
        sol.wallsAndGates(rooms)
        self.assertEqual(rooms, [[-1]])

if __name__ == '__main__':
    unittest.main()