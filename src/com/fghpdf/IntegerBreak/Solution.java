package com.fghpdf.IntegerBreak;

/**
 * @author fghpdf
 * @date 2020/6/15
 * @link https://leetcode.com/problems/integer-break/
 **/
public class Solution {
    public int integerBreak(int n) {
        // n is not less than 2 and not larger than 58
        if (n == 2) {
            return 1;
        }

        if (n == 3) {
            return 2;
        }

        int result = 1;
        // n >= 5 cut 3
        while (n >= 5) {
            result *= 3;
            n -= 3;
        }

        // n <= 4 no cut
        result *= n;

        return result;
    }
}
