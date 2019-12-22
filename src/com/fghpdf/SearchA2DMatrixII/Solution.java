package com.fghpdf.SearchA2DMatrixII;

/**
 * @author fghpdf
 * @date 2019/12/22
 * https://leetcode.com/problems/search-a-2d-matrix-ii/
 * it is a binary search tree
 * the root is matrix[0][last]
 * left is smaller than root, right is bigger than root
 **/
public class Solution {
	public boolean searchMatrix(int[][] matrix, int target) {
		if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
			return false;
		}

		int col = matrix[0].length - 1;
		int row = 0;
		while (col >= 0 && row <= matrix.length - 1) {
			if (matrix[row][col] == target) {
				return true;
			} else if (target < matrix[row][col]) {
				col--;
			} else if (target > matrix[row][col]) {
				row++;
			}
		}

		return false;
	}
}
