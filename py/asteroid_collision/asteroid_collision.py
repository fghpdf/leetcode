'''
Author: fghpdf
Date: 2022-01-19 08:56:54
LastEditTime: 2022-01-19 09:35:38
LastEditors: fghpdf
'''
from math import prod
from typing import List
import unittest

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 0:
            return []

        asteroidStack = []
        for asteroid in asteroids:
            while len(asteroidStack) > 0 and asteroid < 0 and asteroidStack[-1] > 0:
              if asteroidStack[-1] == -asteroid:
                # both explode
                asteroidStack.pop()
                break
              if asteroidStack[-1] < -asteroid:
                # last explode
                asteroidStack.pop()
                continue
              if asteroidStack[-1] > -asteroid:
                # coming explode
                break
            else:
              asteroidStack.append(asteroid)
        return asteroidStack

class TestSolution(unittest.TestCase):
    def testAsteroidCollision(self):
        sol = Solution()
        self.assertEqual(sol.asteroidCollision([-2,-1,1,2]), [-2,-1,1,2])
        self.assertEqual(sol.asteroidCollision([5,10,-5]), [5,10])
        self.assertEqual(sol.asteroidCollision([8,-8]), [])
        self.assertEqual(sol.asteroidCollision([10,2,-5]), [10])
        

if __name__ == '__main__':
    unittest.main()