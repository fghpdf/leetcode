'''
Author: fghpdf
Date: 2021-10-09 10:42:01
LastEditTime: 2021-10-09 11:19:34
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
      if len(image) == 0 or len(image[0]) == 0:
        return image

      color = image[sr][sc]
      if color != newColor:
        image = self.backtrack(image, color, sr, sc, newColor)

      return image

  def backtrack(self, image: List[List[int]], color: int, sr: int, sc: int, newColor: int) -> List[List[int]]:
    # edge will end
    if (sr < 0 or sr >= len(image)) or (sc < 0 or sc >= len(image[0])):
      return image

    if color != image[sr][sc]:
      return image

    image[sr][sc] = newColor
    
    # step left
    image = self.backtrack(image, color, sr, sc - 1, newColor)
    # step up
    image = self.backtrack(image, color, sr - 1, sc, newColor)
    # step right
    image = self.backtrack(image, color, sr, sc + 1, newColor)
    # step down
    image = self.backtrack(image, color, sr + 1, sc, newColor)

    return image
    
    

class TestFloodFill(unittest.TestCase):
  def test_flood_fill(self):
    sol = Solution()
    self.assertEqual(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]])
    self.assertEqual(sol.floodFill([[0,0,0],[0,0,0]], 0, 0, 2), [[2,2,2],[2,2,2]])

if __name__ == '__main__':
  unittest.main()