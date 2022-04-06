from typing import Counter, List
import unittest
import itertools

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        if len(arr) == 0:
          return 0

        c = Counter(arr)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: res += c[i] * (c[i] - 1) * (c[i] - 2) / 6
            elif i == j != k: res += c[i] * (c[i] - 1) / 2 * c[k]
            elif k > i and k > j: res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)


class TestSolution(unittest.TestCase):
    def testThreeSumMulti(self):
        sol = Solution()
        self.assertEqual(sol.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8), 20)
        self.assertEqual(sol.threeSumMulti(arr = [1,1,2,2,2,2], target = 5), 12)

if __name__ == '__main__':
    unittest.main()