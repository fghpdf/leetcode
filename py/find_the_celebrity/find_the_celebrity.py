def knows(a: int, b: int) -> bool:
    return True

class Solution:
    def findCelebrity(self, n: int) -> int:
        possibleCelebrity = 0
        for i in range(1,n):
          # if true, then possibleCelebrity cannot be the real celebrity because real celebrity should know nobody
          # if false, then i cannot be the celebrity because celebrity should be known by all the other ones
          if knows(possibleCelebrity, i):
              possibleCelebrity = i

        for i in range(n):
          # this possibleCelebrity do know i
          # real celebrity should know nobody, so the possibleCelebrity is not the real celebrity
          if i != possibleCelebrity and knows(possibleCelebrity, i):
              return -1

          # this possibleCelebrity are not known by i
          # real celebrity should be known by all the other ones, so the possibleCelebrity is not the real celebrity
          if (i != possibleCelebrity and not knows(i, possibleCelebrity)):
            return -1

        return possibleCelebrity
