import unittest

class Solution:
    def maximum69Number (self, num: int) -> int:
        if num == 0:
            return 0

        res = num
        arr = list(map(int, str(num)))
        for i in range(len(arr)):
          if arr[i] == 9:
            continue
          newArr = arr[:]
          newArr[i] = 9
          newNum = int(''.join(str(n) for n in newArr))
          if newNum >= res:
            res = newNum

        return res

class TestSolution(unittest.TestCase):
    def testMaximum69Number(self):
        sol = Solution()
        self.assertEqual(sol.maximum69Number(9669), 9969)
        self.assertEqual(sol.maximum69Number(9996), 9999)
        self.assertEqual(sol.maximum69Number(9999), 9999)

if __name__ == '__main__':
    unittest.main()