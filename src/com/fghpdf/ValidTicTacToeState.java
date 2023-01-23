package com.fghpdf;

class Solution {

    int numX;
    int numO;

    public boolean validTicTacToe(String[] board) {
        // can't be two winners AND X has as many spots as O or 1 more max

        // numbers don't add up
        if (!numXPossible(board))
            return false;

        boolean winnerO = checkForWin(board, 'O');
        boolean winnerX = checkForWin(board, 'X');

        // can't both be winners
        if (winnerO && winnerX)
            return false;

        // if X won, it must have had an extra move
        if (winnerX && this.numX - this.numO != 1)
            return false;

        // if O won, the moves must be equal
        if (winnerO && this.numX - this.numO != 0)
            return false;

        return true;
    }

    // true indicates the number of Xs to Os is possible
    public boolean numXPossible(String[] board) {

        this.numX = 0;
        this.numO = 0;

        for (String ln : board) {
            for (int i = 0; i < 3; i++) {
                if (ln.charAt(i) == 'X')
                    this.numX++;
                else if (ln.charAt(i) == 'O')
                    this.numO++;
            }
        }

        // X must either be one ahead or the same
        return this.numX - this.numO == 0 || this.numX - this.numO == 1;
    }

    public boolean checkForWin(String[] board, char c) {
        // check horizontal
        for (String ln : board) {
            for (int i = 0; i < 3; i++) {
                if (ln.charAt(0) == c && ln.charAt(1) == c && ln.charAt(2) == c) {
                    return true;
                }
            }
        }

        // check vert
        if ((board[0].charAt(0) == c && board[1].charAt(0) == c && board[2].charAt(0) == c) || (board[0].charAt(1) == c && board[1].charAt(1) == c && board[2].charAt(1) == c) || (board[0].charAt(2) == c && board[1].charAt(2) == c && board[2].charAt(2) == c))
            return true;

        // check diagonal
        if ((board[0].charAt(0) == c && board[1].charAt(1) == c && board[2].charAt(2) == c) || (board[0].charAt(2) == c && board[1].charAt(1)  == c && board[2].charAt(0) == c))
            return true;

        return false;
    }
}
