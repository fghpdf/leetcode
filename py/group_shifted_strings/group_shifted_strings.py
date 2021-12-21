from typing import List
import unittest

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if len(strings) == 0:
            return []

        resMap = {}
        for s in strings:
          key = ()
          for i in range(len(s)-1):
            diff = 26 + ord(s[i+1]) - ord(s[i])
            key += (diff%26,)

          resMap[key] = resMap.get(key, []) + [s]
        
        return list(resMap.values())

class TestSolution(unittest.TestCase):
    def testGroupStrings(self):
        sol = Solution()
        self.assertEqual(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]), [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]])
        self.assertEqual(sol.groupStrings(["a"]), [["a"]])

if __name__ == '__main__':
    unittest.main()