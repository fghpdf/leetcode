from collections import defaultdict
import unittest

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
          return 0

        left = 0
        right = 0
        counts = defaultdict(int)

        while right < len(s):
          # add item into window
          counts[s[right]] += 1
          # extend right
          right += 1
          
          if len(counts) > 2:
            # remove item from window
            counts[s[left]] -= 1
            if not counts[s[left]]:
              del counts[s[left]]
            # shrink left
            left += 1

        return right - left


class TestSolution(unittest.TestCase):
    def testLengthOfLongestSubstringTwoDistinct(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstringTwoDistinct("eceba"), 3)
        self.assertEqual(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb"), 5)

if __name__ == '__main__':
    unittest.main()