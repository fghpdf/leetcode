'''
Author: fghpdf
Date: 2022-02-16 08:48:30
LastEditTime: 2022-02-16 08:59:10
LastEditors: fghpdf
'''
from typing import List
import unittest

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if len(employees) == 0:
            return 0

        res = 0
        for employee in employees:
          if id == employee.id:
            res += employee.importance
            for subId in employee.subordinates:
              res += self.getImportance(employees, subId)

        return res

class TestSolution(unittest.TestCase):
    def testGetImportance(self):
        sol = Solution()
        self.assertEqual(sol.getImportance(employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1), 11)
        self.assertEqual(sol.getImportance(employees = [[1,2,[5]],[5,-3,[]]], id = 5), -3)

if __name__ == '__main__':
    unittest.main()
