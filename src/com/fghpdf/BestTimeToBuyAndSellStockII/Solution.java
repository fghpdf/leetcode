package com.fghpdf.BestTimeToBuyAndSellStockII;

/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
 * @author fghpdf
 *
 * this question isn't dynamic question.
 * first the prices you can split to small array.
 * and then you can find if this price bigger, you can sold because of the last
 * result is add all prices.
 */
public class Solution {
	public int maxProfit(int[] prices) {
		int result = 0;
		for (int i = 0; i < prices.length - 1; i++) {
			if (prices[i + 1] > prices[i]) {
				result += prices[i + 1] - prices[i];
			}
		}

		return result;
	}
}
