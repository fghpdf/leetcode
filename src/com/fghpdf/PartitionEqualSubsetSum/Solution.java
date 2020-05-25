package com.fghpdf.PartitionEqualSubsetSum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2020/5/21
 * @link https://leetcode.com/problems/partition-equal-subset-sum/
 * status is { capacity: sum/2, nums }
 * chose is { put in or not}
 * dp[i][j] is that No.i-1 items sum can equal j in two ways
 * base case dp[0][...] is false beacuse no items can put
 * dp[...][0] is true because no capacity needs items to put in
 **/
public class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        // odd sum will never get two part can equal
        if (sum % 2 != 0) {
            return false;
        }

        // init
        // dp[i][j] is that No.i-1 items sum can equal j in two ways
        // put in or not
        boolean[][] dp = new boolean[nums.length+1][sum/2+1];
        // no items
        Arrays.fill(dp[0], false);
        // no capacity
        for (int i = 0; i <= nums.length; i++) {
            dp[i][0] = true;
        }

        // loop [1, nums.length]
        for (int i = 1; i <= nums.length; i++) {
            for (int j = 0; j <= sum / 2; j++) {
                // can't put in cause no enough value
                if (j - nums[i - 1] > 0 ) {
                    dp[i][j] = dp[i-1][j];
                } else {
                    // put in or not
                    dp[i][j] = dp[i-1][j] || dp[i-1][j - nums[i-1]];
                }
            }
        }

        return dp[nums.length][sum/2];
    }

    private static class Segment {
        int start;
        int length;
        Segment(int start, int length) {
            this.start = start;
            this.length = length;
        }
    }

    public static void main(String[] args) {
        Map<Integer, Integer> startPosition = new HashMap<>();
        Map<Integer, Integer> startToLength = new HashMap<>();
        Map<Integer, Integer> numberToSegments = new HashMap<>();

        int[] nums = new int[]{0,2,3,1,0,1,1,3,4};

        int prev = nums[0];
        int start = 0;

        // edge
        startPosition.put(start, nums[0]);
        startToLength.put(start, 1);
        numberToSegments.put(nums[0], 1);

        for (int i = 1; i < nums.length; i++) {
            if (prev == nums[i]) {
                startToLength.merge(start, 1, Integer::sum);
            } else {
                start = i;
                startToLength.put(start, 1);
                startPosition.put(start, nums[i]);
                numberToSegments.merge(nums[i], 1, Integer::sum);
            }

            prev = nums[i];
        }

        int[] startIndex = startToLength.keySet().stream().mapToInt(Number::intValue).toArray();
        Arrays.sort(startIndex);

        int prevStart = startIndex[0];
        int maxLength = 0;
        for (int i = 1; i < startIndex.length; i++) {
            int nextStart = startToLength.get(prevStart) + prevStart + 1;
            int currentLength = startToLength.get(startIndex[i]);
            if (startToLength.containsKey(nextStart)
                    && startPosition.get(prevStart).equals(nums[nextStart])
                    && numberToSegments.get(nums[nextStart]) >= 3) {
                maxLength = Math.max(startToLength.get(nextStart) + 1 + currentLength, maxLength);
            } else {
                if (numberToSegments.get(nums[startIndex[i]]) >= 2) {
                    currentLength++;
                }
                maxLength = Math.max(currentLength, maxLength);
            }

            prevStart = startIndex[i];
        }

        System.out.println(maxLength);
    }
}
