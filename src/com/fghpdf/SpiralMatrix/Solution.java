package com.fghpdf.SpiralMatrix;

import java.util.ArrayList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2019/11/23
 * https://leetcode.com/problems/spiral-matrix/
 * should do sure the direction
 **/
public class Solution {
	public List<Integer> spiralOrder(int[][] matrix) {
		List<Integer> result = new ArrayList<>();
		int rowLength = matrix.length - 1;
		if (rowLength < 0) {
			return result;
		}
		int colLength = matrix[0].length - 1;

		int row = 0;
		int col = 0;
		String direction = "right";

		while (row <= rowLength && col <= colLength) {
			if ("right".equals(direction)) {
				for (int i = col; i <= colLength; i++) {
					result.add(matrix[row][i]);
				}
				direction = changeDirection(direction);
				row++;
				continue;
			}

			if ("down".equals(direction)) {
				for (int i = row; i <= rowLength; i++) {
					result.add(matrix[i][colLength]);
				}
				direction = changeDirection(direction);
				colLength--;
				continue;
			}

			if ("left".equals(direction)) {
				for (int i = colLength; i >= col ; i--) {
					result.add(matrix[rowLength][i]);
				}
				direction = changeDirection(direction);
				rowLength--;
				continue;
			}

			if ("up".equals(direction)) {
				for (int i = rowLength; i >= row; i--) {
					result.add(matrix[i][col]);
				}
				direction = changeDirection(direction);
				col++;
				continue;
			}
		}

		return result;
	}

	private String changeDirection(String direction) {
		switch (direction) {
			case "right":
				return "down";
			case "down":
				return "left";
			case "left":
				return "up";
			case "up":
				return "right";
			default:
				return "";
		}
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[][] matrix = new int[3][4];
		matrix[0] = new int[]{1, 2, 3, 4};
		matrix[1] = new int[]{5, 6, 7, 8};
		matrix[2] = new int[]{10, 11, 12, 13};
		System.out.println(sol.spiralOrder(matrix));
	}
}
