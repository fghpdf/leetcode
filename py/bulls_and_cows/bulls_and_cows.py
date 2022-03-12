from collections import Counter
import unittest

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if len(secret) == 0 or len(guess) == 0:
          return ""

        bulls = 0
        secretC = Counter(secret)
        guessC = Counter(guess)
        for i in range(len(secret)):
          if int(secret[i]) - int(guess[i]) == 0:
            bulls += 1
            secretC[secret[i]] -= 1
            guessC[secret[i]] -= 1

        cows = 0
        for item in guessC.items():
          if secretC[item[0]] == 0:
            continue
          if secretC[item[0]] >= item[1]:
            cows += item[1]
          else:
            cows += secretC[item[0]]
        
        return str(bulls) + "A" + str(cows) + "B"
        

class TestSolution(unittest.TestCase):
    def testGetHint(self):
        sol = Solution()
        self.assertEqual(sol.getHint(secret = "1807", guess = "7810"), "1A3B")
        self.assertEqual(sol.getHint(secret = "1123", guess = "0111"), "1A1B")

if __name__ == "__main__":
    unittest.main()