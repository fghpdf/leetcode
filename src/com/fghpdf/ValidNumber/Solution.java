package com.fghpdf.ValidNumber;

/**
 * @author fghpdf
 * @date 2020/6/5
 * @link https://leetcode.com/problems/valid-number/
 **/
public class Solution {
    public boolean isNumber(String s) {
        if (s == null || s.length() == 0) {
            return false;
        }

        s = s.trim();

        boolean havePoint = false;
        boolean haveE = false;
        boolean haveNumber = false;
        boolean haveNumberAfterE = false;

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if ('0' <= currentChar && currentChar <= '9') {
                haveNumber = true;
                haveNumberAfterE = true;
            } else if (currentChar == '.') {
                // no repeated
                // e must after point
                if (havePoint || haveE) {
                    return false;
                }

                havePoint = true;
            } else if (currentChar == 'e') {
                // no repeated
                // number must be seen before e
                if (haveE || !haveNumber) {
                    return false;
                }

                haveE = true;
                haveNumberAfterE = false;
            } else if (currentChar == '-' || currentChar == '+') {
                // -1E-16 valid
                if (i != 0 && s.charAt(i-1) != 'e') {
                    return false;
                }
            } else {
                return false;
            }
        }

        return haveNumber && haveNumberAfterE;
    }
}
