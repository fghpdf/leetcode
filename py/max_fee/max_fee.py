from typing import List
import unittest

class MaxFeeProcess:
    def calcMaxFee(self, transactions: List[List[int]], size: int) -> int:
      if len(transactions) == 0:
          return 0
      n = len(transactions)
      dp = [[0 for i in range(size+1)] for j in range(n+1)]

      for i in range(1, n+1):
        for j in range(1, size+1):
          if j-transactions[i-1][1] < 0:
            # no more size
            dp[i][j] = dp[i-1][j]
          else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-transactions[i-1][1]]+transactions[i-1][2])

      return dp[n][size]

class TestMaxFeeProcess(unittest.TestCase):
    def testCalcMaxFee(self):
        process = MaxFeeProcess()
        self.assertEqual(process.calcMaxFee([[1,5,10], [2,4,5], [3,6,3]], 10), 15)

if __name__ == '__main__':
    unittest.main()