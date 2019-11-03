package com.fghpdf.ReverseBits;

/**
 * @author fghpdf
 * @date 2019/10/26
 *
 * https://leetcode.com/problems/reverse-bits/
 * bitwise
 * A = 0011 1100
 * B = 0000 1101
 * -----------------
 * A&B = 0000 1100 and
 * A | B = 0011 1101 or
 * A ^ B = 0011 0001 xor
 * ~A= 1100 0011
 * A << 2 = 1111 0000
 * A >> 2 = 1111
 * A>>>2 = 0000 1111
 **/
public class Solution {
	// you need treat n as an unsigned value
	public int reverseBits(int n) {
		int result = 0;
		for (int i = 0; i < 32; i++) {
			result += n & 1;
			n >>>= 1;
			if (i < 31) {
				result <<= 1;
			}
		}
		return result;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		int result = solution.reverseBits(011);
		System.out.println(result);
	}
}
