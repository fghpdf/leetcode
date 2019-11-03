package com.fghpdf.NumberOfOneBits;

/**
 * @author fghpdf
 * @date 2019/10/27
 *
 * https://leetcode.com/problems/number-of-1-bits/
 * 0 & 1 = 0
 * 1 & 1 = 1
 * so we can move bit and do &
 * https://leetcode.com/problems/number-of-1-bits/discuss/55099/Simple-Java-Solution-Bit-Shifting/56672
 **/
public class Solution {
	// you need to treat n as an unsigned value
	public int hammingWeight(int n) {
		int c = 0;
		while (n != 0) {
			c += (n & 1);
			n >>>= 1;
		}
		return c;
	}
}
