from typing import List
import unittest

class HitCounter:
    times: List[int]
    hits: List[int]

    def __init__(self):
        self.times = [0]*300
        self.hits = [0]*300

    def hit(self, timestamp: int) -> None:
        index = timestamp % 300
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp: int) -> int:
        res = 0
        for i in range(300):
            if (timestamp - self.times[i]) < 300:
                res += self.hits[i]

        return res

class TestSolution(unittest.TestCase):
    def testHitCounter(self):
        h = HitCounter()
        h.hit(1)
        h.hit(2)
        h.hit(3)
        self.assertEqual(h.getHits(4), 3)
        h.hit(300)
        self.assertEqual(h.getHits(300), 4)
        self.assertEqual(h.getHits(301), 3)

if __name__ == '__main__':
    unittest.main()