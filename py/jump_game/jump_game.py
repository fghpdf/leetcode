from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curMax = nums[0]
        for i in range(1, len(curMax)):
            if curMax < i:
                return False

            curMax = max(curMax, i + nums[i])

        return True
