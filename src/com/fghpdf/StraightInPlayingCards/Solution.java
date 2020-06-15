package com.fghpdf.StraightInPlayingCards;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2020/6/15
 * @link https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
 **/
public class Solution {
    public boolean isStraight(int[] nums) {
        // like [0, 0, 1, 3, 5]
        Arrays.sort(nums);

        // max is nums[4]
        // min is the number behind 0
        // 0 can't more than 2
        int minIndex = 0;
        for (int i = 0; i < 4; i++) {
            if (nums[i] == 0) {
                minIndex++;
            } else {
                // no repeat
                if (nums[i] == nums[i+1]) {
                    return false;
                }
            }
        }

        return nums[4] - nums[minIndex] < 5;
    }
}
