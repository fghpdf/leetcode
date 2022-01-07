'''
Author: fghpdf
Date: 2022-01-07 08:53:42
LastEditTime: 2022-01-07 09:18:08
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 0:
            return []

        pointDict = {}
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            distancePoints = pointDict.get(distance, [])
            distancePoints.append(point)
            pointDict[distance] = distancePoints

        res = []
        for key in sorted(pointDict.keys()):
            points = pointDict[key]
            if k == 0:
              return res
            
            if k >= len(points):
              res.extend(points[:])
              k -= len(points)
            else:
              res.extend(points[:k])
              return res

        return res
                
class TestSolution(unittest.TestCase):
    def testKClosest(self):
        sol = Solution()
        self.assertEqual(sol.kClosest(points = [[1,3],[-2,2]], k = 1), [[-2,2]])
        self.assertEqual(sol.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2), [[3,3],[-2,4]])

if __name__ == "__main__":
    unittest.main()