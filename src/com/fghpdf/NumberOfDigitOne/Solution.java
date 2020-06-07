package com.fghpdf.NumberOfDigitOne;

/**
 * @author fghpdf
 * @date 2020/6/7
 * @link https://leetcode.com/problems/number-of-digit-one/
 **/
public class Solution {
    public int countDigitOne(int n) {

        if (n <= 0) {
            return 0;
        }
        int q = n, x = 1, ans = 0;
        do {
            int digit = q % 10;
            q /= 10;
            ans += q * x;
            if (digit == 1) {
                ans += n % x + 1;
            }
            if (digit >  1) {
                ans += x;
            }
            x *= 10;
        } while (q > 0);
        return ans;

    }
}
