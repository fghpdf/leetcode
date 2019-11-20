package com.fghpdf.RotateImage;

/**
 * @author fghpdf
 * @date 2019/11/20
 * https://leetcode.com/problems/rotate-image/
 * first reverse up to down, then swap the symmetry
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
 **/
public class Solution {
	public void rotate(int[][] matrix) {
		int topRow = 0;
		int bottomRow = matrix.length - 1;
		while (topRow < bottomRow) {
			int[] temp = matrix[topRow];
			matrix[topRow] = matrix[bottomRow];
			matrix[bottomRow] = temp;
			topRow++;
			bottomRow--;
		}

		for (int i = 0; i < matrix.length - 1; i++) {
			for (int j = i + 1; j < matrix[i].length; j++) {
				int temp = matrix[i][j];
				matrix[i][j] = matrix[j][i];
				matrix[j][i] = temp;
			}
		}
	}
}
