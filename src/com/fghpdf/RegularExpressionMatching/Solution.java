package com.fghpdf.RegularExpressionMatching;

/**
 * @author fghpdf
 * @date 2020/6/5
 * @link https://leetcode.com/problems/regular-expression-matching/
 **/
public class Solution {
    public boolean isMatch(String s, String p) {
        if (s == null || p == null) {
            return false;
        }

        // dp is s and p can match
        // dp[s][p]
        boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];

        // init
        // 0 0 present before 0
        dp[0][0] = true;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '*' && dp[0][i-1]) {
                dp[0][i+1] = true;
            }
        }

        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < p.length(); j++) {
                if (p.charAt(j) == s.charAt(i)) {
                    dp[i+1][j+1] = dp[i][j];
                }

                if (p.charAt(j) == '.') {
                    dp[i+1][j+1] = dp[i][j];
                }

                if (p.charAt(j) == '*') {
                    // ignore *
                    if (p.charAt(j-1) != s.charAt(i) && p.charAt(j-1) != '.') {
                        dp[i+1][j+1] = dp[i+1][j-1];
                    } else {
                        dp[i+1][j+1] = (dp[i+1][j] || dp[i][j+1] || dp[i+1][j-1]);
                    }
                }
            }
        }

        return dp[s.length()][p.length()];
    }

}
