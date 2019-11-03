package com.fghpdf.PascalTriangle2;

import java.util.ArrayList;
import java.util.List;

/**
 * pascal triangle return row
 * @author fghpdf
 * https://leetcode.com/problems/pascals-triangle-ii/discuss/38420/Here-is-my-brief-O(k)-solution/36288
 */
public class Solution {
	public List<Integer> getRow(int rowIndex) {
		List<List<Integer>> triangle = new ArrayList<>();

		List<Integer> firstRow = new ArrayList<>();
		firstRow.add(1);
		triangle.add(firstRow);


		List<Integer> twoRow = new ArrayList<>();
		twoRow.add(1);
		twoRow.add(1);
		triangle.add(twoRow);

		for (int i = 3; i <= rowIndex + 1; i++) {
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

		return triangle.get(rowIndex);
	}
}
