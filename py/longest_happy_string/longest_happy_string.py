import unittest
from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
      max_heap = []
      if a != 0:
            heappush(max_heap, (-a, 'a'))
      if b != 0:
          heappush(max_heap, (-b, 'b'))
      if c != 0:
          heappush(max_heap, (-c, 'c'))
      s = []
      while max_heap:
          first, char1 = heappop(max_heap)
          if len(s) >= 2 and s[-1] == s[-2] == char1:
              if not max_heap:
                  return ''.join(s)
              second, char2 = heappop(max_heap)
              s.append(char2)
              second += 1
              if second != 0:
                  heappush(max_heap, (second, char2))
              heappush(max_heap, (first, char1))
              continue

          s.append(char1)
          first += 1
          if first != 0:
            heappush(max_heap, (first, char1))
      return ''.join(s)

class TestSolution(unittest.TestCase):
    def testLongestDiverseString(self):
        sol = Solution()
        self.assertEqual(sol.longestDiverseString(a = 1, b = 1, c = 7), "ccaccbcc")
        self.assertEqual(sol.longestDiverseString(a = 7, b = 1, c = 0), "aabaa")

if __name__ == "__main__":
    unittest.main()