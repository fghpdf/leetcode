package com.fghpdf.DecodeWays;

/**
 * @author fghpdf
 * @date 2019/11/29
 * https://leetcode.com/problems/decode-ways/
 * dp question
 * first should set dp[0] is 1
 * dp[n] = dp[n-1] + dp[n-2]
 * like 226 [2 2 6, 22 6, 2 26]
 * n = 1 => [2 2 6] => dp[1] = 1
 * n = 2 first is 2 second is 22
 * and is [2 2 6, 22 6] => dp[2] = dp[1] + 1
 * n = 3 first is 6, second is 26
 * and is [2 2 6, 2 26] => dp[3] = dp[2] + dp[1]
 *
 **/
public class Solution {
	public int numDecodings(String s) {
		if (s.isEmpty()) {
			return 0;
		}

		int n = s.length();
		int[] dp = new int[n+1];
		// special for sure dp[n] is right
		dp[0] = 1;
		dp[1] = s.charAt(0) == '0' ? 0 : 1;
		for (int i = 2; i <= n; i++) {
			int first = Integer.parseInt(s.substring(i-1, i));
			int second = Integer.parseInt(s.substring(i-2, i));
			if (first > 0 && first <= 9) {
				dp[i] += dp[i-1];
			}
			if (second >= 10 && second <= 26) {
				dp[i] += dp[i-2];
			}
		}
		return dp[n];
	}
}
