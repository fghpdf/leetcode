'''
Author: fghpdf
Date: 2021-10-16 11:54:58
LastEditTime: 2021-10-16 11:54:59
LastEditors: fghpdf
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in xrange(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans