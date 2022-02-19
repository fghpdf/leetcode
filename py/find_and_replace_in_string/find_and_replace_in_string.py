from typing import List
import unittest

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        if not s and not indices and not sources and not targets:
          return ""

        preReplace = {}
        # check
        for index, source in enumerate(sources):
          if s[indices[index]:].find(source) == 0:
            preReplace[indices[index]] = [indices[index]+len(source), targets[index]]

        res = []
        nextValidIndex = 0
        for i, c in enumerate(s):
          if i != nextValidIndex:
            continue
          if preReplace.get(i):
            res.append(preReplace[i][1])
            nextValidIndex = preReplace[i][0]
          else:
            res.append(c)
            nextValidIndex = i + 1
        
        return ''.join(res)

class TestSolution(unittest.TestCase):
    def testFindReplaceString(self):
      sol = Solution()
      self.assertEqual(sol.findReplaceString("wreorttvosuidhrxvmvo",[14,12,10,5,0,18],["rxv","dh","ui","ttv","wreor","vo"],["frs","c","ql","qpir","gwbeve","n"]), "gwbeveqpirosqlcfrsmn")
      self.assertEqual(sol.findReplaceString(s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]), "eeebffff")
      self.assertEqual(sol.findReplaceString(s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]), "eeecd")

if __name__ == '__main__':
    unittest.main()