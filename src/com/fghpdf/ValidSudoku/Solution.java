package com.fghpdf.ValidSudoku;

import java.util.HashSet;
import java.util.Set;

/**
 * @author fghpdf
 * @date 2019/11/18
 * https://leetcode.com/problems/valid-sudoku/
 * '4' in row 7 is encoded as "(4)7".
 * '4' in column 7 is encoded as "7(4)".
 * '4' in the top-right block is encoded as "0(4)2".
 **/
public class Solution {
	public boolean isValidSudoku(char[][] board) {
		Set seen = new HashSet<>();
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				if (board[i][j] != '.') {
					String b = "(" + board[i][j] + ")";
					if (!seen.add(b + i) || !seen.add(j + b) || !seen.add(i/3 + b + j/3)) {
						return false;
					}
				}
			}
		}
		return true;
	}
}
