'''
Author: fghpdf
Date: 2022-01-27 09:14:05
LastEditTime: 2022-01-27 09:22:51
LastEditors: fghpdf
'''
from collections import defaultdict
from itertools import combinations
from typing import Counter, List
import unittest

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[user].append(site)
        patterns = Counter()
        
        for user, sites in users.items():
            patterns.update(Counter(set(combinations(sites, 3))))
        return list(max(sorted(patterns), key=patterns.get))

class TestSolution(unittest.TestCase):
    def testMostVisitedPattern(self):
        sol = Solution()
        self.assertEqual(sol.mostVisitedPattern(username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]), ["home","about","career"])
        self.assertEqual(sol.mostVisitedPattern(username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]), ["a","b","a"])

if __name__ == '__main__':
    unittest.main()
    