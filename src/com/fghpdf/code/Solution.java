package com.fghpdf.code;

/**
 * @author fghpdf
 * @date 2020/6/8
 * @link
 **/
public class Solution {
    public int getMinBus(int[] stations) {
        if (stations.length == 0) {
            return 0;
        }

        if (stations.length == 1) {
            return 1;
        }

        // 获得车站差值
        int prev = stations[0];
        int result = 0;
        // 0 d
        int last = 0;
        for (int i = 1; i < stations.length; i++) {
            // 负数代表最少需要 1 辆车
            // 正数和 0 代表最少需要 2 辆车
            result += stations[i] - prev < 0 ? 0 : 1;
            prev = stations[i];
        }

        return result;
    }

    public static void main(String[] args) {
        // test case

    }
}
