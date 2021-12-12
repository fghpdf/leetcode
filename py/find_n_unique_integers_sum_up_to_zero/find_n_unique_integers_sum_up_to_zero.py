from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 0:
            return []

        res = []
        toN = n // 2
        if n % 2 != 0:
          toN += 1
        for i in range(n, toN, -1):
          res.append(i)
          res.append(-i)

        if len(res) != n:
            res.append(0)

        return res