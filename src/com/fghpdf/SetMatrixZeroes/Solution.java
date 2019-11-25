package com.fghpdf.SetMatrixZeroes;

/**
 * @author fghpdf
 * @date 2019/11/25
 * https://leetcode.com/problems/set-matrix-zeroes/
 * the key point is col first element and row first element is zero
 * when element is zero
 * so set first element in row and col.
 **/
public class Solution {
	public void setZeroes(int[][] matrix) {
		boolean isFirstZeroInColumn = false;
		int rowSize = matrix.length;
		int colSize = matrix[0].length;

		for (int i = 0; i < rowSize; i++) {
			if (matrix[i][0] == 0) {
				isFirstZeroInColumn = true;
			}
			for (int j = 1; j < colSize; j++) {
				if (matrix[i][j] == 0) {
					matrix[i][0] = 0;
					matrix[0][j] = 0;
				}
			}
		}

		for (int i = rowSize - 1; i >= 0; i--) {
			for (int j = colSize - 1; j >= 1; j--) {
				if (matrix[i][0] == 0 || matrix[0][j] == 0) {
					matrix[i][j] = 0;
				}
			}
			if (isFirstZeroInColumn) {
				matrix[i][0] = 0;
			}
		}
	}
}
