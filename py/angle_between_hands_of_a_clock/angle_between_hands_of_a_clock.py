import unittest

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # In 12 hours Hour hand complete whole circle and cover 360°
        # So, 1 hour = 360° / 12 = 30°

        # Since 1 hours = 30°
        # In 1 minute, hours hand rotate -> 30° / 60 = 0.5°
        # So total angle because of minutes by hour hand is minutes/60 * 30 or minutes * 0.5
        # In 60 minutes Minute Hand completes whole circle and cover 360°.
        # So, 1 minute -> 360° / 60 = 6°
        h = (hour%12*30) + (minutes/60*30)
        m = minutes * 6

        angle = abs(m-h)

        if angle > 180:
            return 360 - angle

        return angle

class TestSolution(unittest.TestCase):
    def testAngleClock(self):
        sol = Solution()
        self.assertEqual(sol.angleClock(12, 30), 165)
        self.assertEqual(sol.angleClock(3, 30), 75)
        self.assertEqual(sol.angleClock(3, 15), 7.5)
        self.assertEqual(sol.angleClock(4, 50), 155)
        self.assertEqual(sol.angleClock(12, 0), 0)

if __name__ == '__main__':
    unittest.main()