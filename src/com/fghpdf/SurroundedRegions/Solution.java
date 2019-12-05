package com.fghpdf.SurroundedRegions;

/**
 * @author fghpdf
 * @date 2019/12/5
 * https://leetcode.com/problems/surrounded-regions/
 * DFS
 * when found O, use dfs to alter connected O to *
 * After that, alter * to O
 **/
public class Solution {
	public void solve(char[][] board) {
		if (board == null || board.length == 0) {
			return;
		}

		int rowLength = board.length;
		int colLength = board[0].length;

		// from first and last col O element to *
		for (int i = 0; i < rowLength; i++) {
			if (board[i][0] == 'O') {
				dfs(i, 1, board);
			}
			if (board[i][colLength - 1] == 'O') {
				dfs(i, colLength - 2, board);
			}
		}

		// from first and last row O element to *
		for (int i = 0; i < colLength; i++) {
			if (board[0][i] == 'O') {
				dfs(1, i, board);
			}

			if (board[rowLength - 1][i] == 'O') {
				dfs(rowLength - 2, i, board);
			}
		}

		// flip O to X, * to O
		for (int i = 1; i < rowLength - 1; i++) {
			for (int j = 1; j < colLength - 1; j++) {
				if (board[i][j] == '*') {
					board[i][j] = 'O';
				} else if (board[i][j] == 'O') {
					board[i][j] = 'X';
				}
			}
		}
	}

	private void dfs(int row, int col, char[][] board) {
		if (row <= 0 || col <= 0 || row >= board.length - 1 || col >= board[0].length - 1 || board[row][col] == 'X') {
			return;
		}

		if (board[row][col] == '*') {
			return;
		}

		if (board[row][col] == 'O') {
			board[row][col] = '*';
		}

		dfs(row + 1, col, board);
		dfs(row - 1, col, board);
		dfs(row, col + 1, board);
		dfs(row, col - 1, board);
	}
}
