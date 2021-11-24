from typing import List
import unittest

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        res = []
        self.backtrack(s, "", res, 0, 0)
        return res
        

    def backtrack(self, s: str, track: str, res: List[str], pos: int, count: int):
        if count > 4:
          return

        if count == 4 and pos == len(s):
          res.append(track[:])
          return

        for i in range(1,4):
          if pos+i > len(s):
            break

          seg = s[pos:pos+i]
          if (seg.startswith('0') and len(seg) > 1) or (i == 3 and int(seg) > 255):
            continue
          
          self.backtrack(s, track + seg[:] + ("" if count == 3 else "."), res, pos+i, count+1)

class TestSolution(unittest.TestCase):
    def testRestoreIpAddresses(self):
        sol = Solution()
        self.assertEqual(sol.restoreIpAddresses("25525511135"), ["255.255.11.135","255.255.111.35"])
        self.assertEqual(sol.restoreIpAddresses("0000"), ["0.0.0.0"])
        self.assertEqual(sol.restoreIpAddresses("1111"), ["1.1.1.1"])


if __name__ == "__main__":
    unittest.main()