package com.fghpdf.BestTimeToBuyAndSellStock;

/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 * @author fghpdf
 *
 * it's dynamic programming question which same as "max subarray problem"
 * we can use Kadane's Algorithm to work out.
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
 */
public class Solution {
	public int maxProfit(int[] prices) {
		int maxCur = 0;
		int maxSoFar = 0;

		for (int i = 1; i < prices.length; i++) {
			maxCur = Math.max(0, maxCur += prices[i] - prices[i - 1]);
			maxSoFar = Math.max(maxCur, maxSoFar);
		}

		return maxSoFar;
	}
}
