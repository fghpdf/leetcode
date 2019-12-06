package com.fghpdf.GasStation;

/**
 * @author fghpdf
 * @date 2019/12/6
 * https://leetcode.com/problems/gas-station/
 * If car starts at A and can not reach B. Any station between A and B
 * can not reach B.(B is the first station that A can not reach.)
 * If the total number of gas is bigger than the total number of cost. There must be a solution.
 **/
public class Solution {
	public int canCompleteCircuit(int[] gas, int[] cost) {
		int gasSum = 0;
		int costSum = 0;

		int startPosition = 0;
		int tank = 0;
		for (int i = 0; i < gas.length; i++) {
			gasSum += gas[i];
			costSum += cost[i];

			tank += gas[i] - cost[i];
			if (tank < 0) {
				startPosition = i + 1;
				tank = 0;
			}
		}

		if (gasSum < costSum) {
			return -1;
		} else {
			return startPosition;
		}
	}
}
