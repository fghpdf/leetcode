package com.fghpdf.KthSmallestElementInASortedMatrix;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @author fghpdf
 * @date 2020/1/7
 * @link https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
 * my way is slow
 * may be can use binary search
 * https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
 **/
public class Solution {
	public int kthSmallest(int[][] matrix, int k) {
		List<Integer> sorted = new ArrayList<>();
		for (int[] row: matrix) {
			sorted.addAll(Arrays.stream(row).boxed().collect(Collectors.toList()));
		}

		Collections.sort(sorted);

		return sorted.get(k-1);
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		int[][] matrix = {{1, 2}, {1, 3}};
		System.out.println(solution.kthSmallest(matrix, 2));
	}
}
