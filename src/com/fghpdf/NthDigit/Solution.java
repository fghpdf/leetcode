package com.fghpdf.NthDigit;

/**
 * @author fghpdf
 * @date 2020/6/7
 * @link https://leetcode.com/problems/nth-digit/
 **/
public class Solution {
    public int findNthDigit(int n) {
        int start = 1;
        int rangeLen = 1;
        long base = 9;
        // n - 9*1 - 9*10*2 - 9*100*3 - ...
        while (n > base * rangeLen) {
            n -= base * rangeLen;
            rangeLen++;
            base *= 10;
            start *= 10;
        }

        int target = start + (n-1) / rangeLen;
        int reminder = (n - 1) % rangeLen;
        return Character.getNumericValue(Integer.toString(target).charAt(reminder));
    }
}
