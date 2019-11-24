package com.fghpdf.MergeIntervals;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Stack;

/**
 * @author fghpdf
 * @date 2019/11/24
 * https://leetcode.com/problems/merge-intervals/
 * first sort array by first element
 * and then compare second and last element
 **/
public class Solution {
	public int[][] merge(int[][] intervals) {
		Stack<Integer> queue = new Stack<>();
		if (intervals.length <= 1) {
			return intervals;
		}
		Arrays.sort(intervals, Comparator.comparingInt(i -> i[0]));
		for (int[] interval : intervals) {
			int first = interval[0];
			int second = interval[1];

			if (queue.size() == 0) {
				queue.add(first);
				queue.add(second);
				continue;
			}

			int last = queue.peek();
			if (first <= last) {
				queue.pop();
				queue.add(Math.max(second, last));
				continue;
			}

			queue.add(first);
			queue.add(second);
		}

		int[][] result = new int[queue.size() / 2][2];
		for (int i = queue.size() / 2 - 1; i >= 0; i--) {
			result[i][1] = queue.pop();
			result[i][0] = queue.pop();
		}

		return result;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[][] intervals = new int[4][2];
		intervals[0] = new int[]{1, 3};
		intervals[1] = new int[]{2, 6};
		intervals[2] = new int[]{8, 10};
		intervals[3] = new int[]{15, 18};

		System.out.println(Arrays.deepToString(sol.merge(intervals)));
	}
}
