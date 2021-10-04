# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# @author: fghpdf
# @date: 2021/10/04
# @link: https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        # loop [left, right]
        while (left <= right):
            mid = (left + right) // 2

            # bad version is in left when mid is bad
            # bad version is in right when mid is normal
            # bad version is mid when mid is bad and mid - 1 is normal
            # bad version is mid + 1 when mid is normal and mid + 1 is bad
            if isBadVersion(mid):
                if self.isMidBadVersion(mid):
                    return mid
                
                right = mid - 1
            else:
                left = mid + 1



    def isMidBadVersion(self, mid):
        # check mid is bad version
        if not isBadVersion(mid):
            return False

        if mid <= 0:
            return False
        # mid is 1
        if mid == 1:
            return True

        # mid -1 is normal
        if not isBadVersion(mid - 1):
            return True

        return False

        
        