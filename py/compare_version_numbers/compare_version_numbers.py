import unittest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if len(version1) == 0 or len(version2) == 0:
          return 0

        version1Numbers = [int(v)  for v in version1.split('.')]
        version2Numbers = [int(v)  for v in version2.split('.')]

        i = 0
        while i < len(version1Numbers) or i < len(version2Numbers):
          a = version1Numbers[i] if i < len(version1Numbers) else 0
          b = version2Numbers[i] if i < len(version2Numbers) else 0

          if a < b:
            return -1
          elif a > b:
            return 1

          i += 1
        return 0

class TestSolution(unittest.TestCase):
    def testCompareVersion(self):
        sol = Solution()
        self.assertEqual(sol.compareVersion(version1 = "1.01", version2 = "1.001"), 0)
        self.assertEqual(sol.compareVersion(version1 = "1.0", version2 = "1.0.0"), 0)
        self.assertEqual(sol.compareVersion(version1 = "0.1", version2 = "1.1"), -1)
        self.assertEqual(sol.compareVersion(version1 = "1.0.1", version2 = "1"), 1)

if __name__ == '__main__':
    unittest.main()