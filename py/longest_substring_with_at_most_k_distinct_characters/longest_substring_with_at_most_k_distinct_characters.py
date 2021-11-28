from typing import Counter
import unittest

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s) == 0 or k == 0:
            return 0

        window = Counter()

        left = 0
        res = 0

        for right, char in enumerate(s):
          window[char] += 1

          while len(window) > k:
            leftChar = s[left]

            # shrink
            window[leftChar] -= 1

            if window[leftChar] == 0:
              del window[leftChar]

            left += 1

          size = right - left + 1
          res = max(res, size)

        return res


class TestSolution(unittest.TestCase):
    def testLengthOfLongestSubstringKDistinct(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2), 3)
        self.assertEqual(sol.lengthOfLongestSubstringKDistinct(s = "aa", k = 1), 2)

if __name__ == '__main__':
    unittest.main()
