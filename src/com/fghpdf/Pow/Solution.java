package com.fghpdf.Pow;

/**
 * @author fghpdf
 * @date 2019/11/22
 * https://leetcode.com/problems/powx-n/
 * n < 0, 1 / x * x ^ (-n) - 1
 * n == 0, 1
 * n == 2, x * x
 * n % 2 -> (x ^ n/2) ^ 2
 * n % 2 != 0 -> x * (x ^ n/2) ^ 2
 **/
public class Solution {
	public double myPow(double x, int n) {
		if (n < 0) {
			return 1 / x * myPow(1 / x, -(n+1));
		}
		if (n == 0) {
			return 1;
		}
		if (n == 2) {
			return x * x;
		}
		if (n % 2 == 0) {
			return myPow(myPow(x, n/2), 2);
		} else {
			return x * myPow(myPow(x, n/2), 2);
		}
	}
}
