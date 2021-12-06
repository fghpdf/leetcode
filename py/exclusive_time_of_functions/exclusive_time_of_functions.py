from typing import List
import unittest

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if n == 0 or len(logs) == 0:
            return []

        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_index, operation, time = log.split(":")
            fn_index, time = int(fn_index), int(time)

            if operation == "start":
                if stack:
                  res[stack[-1]] += (time - prev_time)
                stack.append(fn_index)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return res

class TestSolution(unittest.TestCase):
    def testExclusiveTime(self):
        sol = Solution()
        self.assertEqual(sol.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]), [3,4])
        self.assertEqual(sol.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]), [8])
        self.assertEqual(sol.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]), [7,1])
        self.assertEqual(sol.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]), [8,1])
        self.assertEqual(sol.exclusiveTime(1, ["0:start:0","0:end:0"]), [1])

if __name__ == '__main__':
    unittest.main()