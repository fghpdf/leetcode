package com.fghpdf.SlidingWindowMaximum;

import java.util.Deque;
import java.util.LinkedList;

/**
 * @author fghpdf
 * @date 2020/6/12
 * @link https://leetcode.com/problems/sliding-window-maximum/
 **/
public class Solution {
    public int[] getMaxInSlidingWindow(int[] nums, int k) {
        int[] result = new int[nums.length - k + 1];
        Deque<Integer> maxIndexIn = new LinkedList<>();

        if (nums.length == 0 || k == 0) {
            // invalid
            return new int[0];
        }

        int resultIndex = 0;

        for (int i = 0; i < nums.length; i++) {

            // 如果数字比里面的大，说明这些数不会是最大值，全部踢出来
            while (!maxIndexIn.isEmpty() && nums[i] >= nums[maxIndexIn.peekLast()]) {
                maxIndexIn.pollLast();
            }

            // 超出滑动窗口，踢出
            if (!maxIndexIn.isEmpty() && i - k >= maxIndexIn.peek()) {
                maxIndexIn.pollFirst();
            }

            // 把当前数索引加入队列中，准备下次的最大值
            maxIndexIn.offer(i);
            if (i >= k - 1) {
                result[resultIndex] = nums[maxIndexIn.peek()];
                resultIndex++;
            }
        }

        return result;
    }
}
