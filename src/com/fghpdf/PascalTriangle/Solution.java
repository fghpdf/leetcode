package com.fghpdf.PascalTriangle;

import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/pascals-triangle/
 * @author fghpdf
 *
 * better solution
 * https://leetcode.com/problems/pascals-triangle/discuss/38141/My-concise-solution-in-Java/36127
 */
public class Solution {
	public List<List<Integer>> generate(int numRows) {
		List<List<Integer>> triangle = new ArrayList<>();

		if (numRows == 0) {
			return triangle;
		}

		List<Integer> firstRow = new ArrayList<>();
		firstRow.add(1);
		triangle.add(firstRow);

		if (numRows == 1) {
			return triangle;
		}

		List<Integer> twoRow = new ArrayList<>();
		twoRow.add(1);
		twoRow.add(1);
		triangle.add(twoRow);

		if (numRows == 2) {
			return triangle;
		}

		for (int i = 3; i <= numRows; i++) {
			List<Integer> row = new ArrayList<>();
			row.add(1);
			List<Integer> lastRow = triangle.get(i - 2);
			int lastRowSize = lastRow.size();
			for (int j = 0; j < lastRowSize - 1; j++) {
				row.add(lastRow.get(j) + lastRow.get(j + 1));
			}
			row.add(1);
			triangle.add(row);
		}

		return triangle;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		List<List<Integer>> result = sol.generate(5);
		for (int i = 0; i < result.size(); i++) {
			System.out.println(result.get(i).size());
		}
	}
}
