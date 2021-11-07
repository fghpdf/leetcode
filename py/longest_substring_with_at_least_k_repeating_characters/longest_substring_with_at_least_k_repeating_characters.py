from typing import List
import unittest

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))

class TestSolution(unittest.TestCase):
    def testLLongestSubstring(self):
        sol = Solution()
        self.assertEqual(sol.longestSubstring(s = "aaabb", k = 3), 3)
        self.assertEqual(sol.longestSubstring(s = "ababbc", k = 2), 5)

if __name__ == '__main__':
    unittest.main()