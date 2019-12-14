package com.fghpdf.NumberOfIslands;

/**
 * @author fghpdf
 * @date 2019/12/14
 * https://leetcode.com/problems/number-of-islands/
 * dfs set visited point to 0
 **/
public class Solution {
	public int numIslands(char[][] grid) {
		int result = 0;
		if (grid.length == 0) {
			return result;
		}

		for (int row = 0; row < grid.length; row++) {
			for (int col = 0; col < grid[0].length; col++) {
				if (grid[row][col] == '1') {
					dfs(grid, row, col);
					result++;
				}
			}
		}
		return result;
	}

	private void dfs(char[][] grid, int row, int col) {
		if (row < 0 || col < 0 || row >= grid.length || col >= grid[0].length ) {
			return;
		}

		if (grid[row][col] != '1') {
			return;
		}

		grid[row][col] = 0;
		dfs(grid, row + 1, col);
		dfs(grid, row - 1, col);
		dfs(grid, row, col + 1);
		dfs(grid, row, col - 1);
	}
}
