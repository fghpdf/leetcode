package com.fghpdf.CountPrimes;

/**
 * @author fghpdf
 * @date 2019/10/31
 *
 * the prime number 2 will present 4, 6, 8 and so on is not prime number
 * so we can get a list no prime number.
 **/
public class Solution {
	public int countPrimes(int n) {
		boolean[] noPrimses = new boolean[n];

		int count = 0;
		for (int i = 2; i < n; i++) {
			if (!noPrimses[i]) {
				count++;

				for (int j = 2; j * i < n; j++) {
					noPrimses[j*i] = true;
				}
			}
		}
		return count;
	}


}
