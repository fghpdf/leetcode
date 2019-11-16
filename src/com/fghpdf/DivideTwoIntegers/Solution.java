package com.fghpdf.DivideTwoIntegers;

/**
 * @author fghpdf
 * @date 2019/11/16
 * The key observation is that the quotient of a division is just the number of times
 * that we can subtract the divisor from the dividend without making it negative.
 **/
public class Solution {
	public int divide(int dividend, int divisor) {
		if (dividend == Integer.MIN_VALUE && divisor == -1 || divisor == 0) {
			return Integer.MAX_VALUE;
		}

		int res = 0;
		boolean sign = (dividend < 0) == (divisor < 0);
		long dvd = Math.abs((long)dividend);
		long dvs = Math.abs((long)divisor);
		while (dvs <= dvd) {
			long temp = dvs;
			long mul = 1L;

			while (dvd >= temp<<1) {
				temp<<=1;
				mul<<=1;
			}
			dvd-=temp;
			res+=mul;
		}
		return sign ? res : -res;
	}
}
