package com.fghpdf.SumOfTwoIntegers;

/**
 * @author fghpdf
 * @date 2019/11/7
 *
 * https://leetcode.com/problems/sum-of-two-integers/
 *
 * Good explain
 * https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
 *
 * bit manipulation question
 * Set union A | B
 * Set intersection A & B
 * Set subtraction A & ~B
 * Set negation ALL_BITS ^ A or ~A
 * Set bit A |= 1 << bit
 * Clear bit A &= ~(1 << bit)
 * Test bit (A & 1 << bit) != 0
 * Extract last bit A&-A or A&~(A-1) or x^(x&(x-1))
 * Remove last bit A&(A-1)
 * Get all 1-bits ~0
 **/
public class Solution {
	public int getSum(int a, int b) {
		return b==0? a:getSum(a^b, (a&b)<<1);
	}
}
