package com.fghpdf.LastNumberInCircle;

/**
 * @author fghpdf
 * @date 2020/6/15
 * @link https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
 **/
public class Solution {
    public int lastRemaining(int n, int m) {
        int result = 0;
        for (int i = 2; i <= n; i++) {
            result = (result + m) % i;
        }

        return result;
    }
}
