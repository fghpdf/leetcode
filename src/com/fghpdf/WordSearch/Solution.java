package com.fghpdf.WordSearch;

/**
 * @author fghpdf
 * @date 2019/11/28
 * https://leetcode.com/problems/word-search/
 *
 * recursion
 * search every direction
 * and only save length to save memory
 **/
public class Solution {
	public boolean exist(char[][] board, String word) {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				if (exist(board, i, j, word.toCharArray(), 0)) {
					return true;
				}
			}
		}
		return false;
	}

	private boolean exist(char[][] board, int row, int col, char[] word, int resultLength) {
		if (resultLength == word.length) {
			return true;
		}

		if (row < 0 || col < 0 || row == board.length || col == board[row].length) {
			return false;
		}

		if (board[row][col] != word[resultLength]) {
			return false;
		}

		// make it invalid in board
		board[row][col] ^= 256;
		boolean result =
				exist(board, row, col + 1, word, resultLength + 1)
				|| exist(board, row, col - 1, word, resultLength + 1)
				|| exist(board, row + 1, col, word, resultLength + 1)
				|| exist(board, row - 1, col, word, resultLength + 1);
		// make it valid in board
		board[row][col] ^= 256;
		return result;
	}
}
