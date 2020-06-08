package com.fghpdf.ReplaceSpace;

/**
 * @author fghpdf
 * @date 2020/6/8
 * @link https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
 **/
public class Solution {
    public String replaceSpace(String s) {
        StringBuilder result = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (' ' == ch) {
                result.append("%20");
                continue;
            }

            result.append(ch);
        }

        return result.toString();
    }
}
