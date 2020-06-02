package com.fghpdf.IntersectionOfTwoArrays;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

/**
 * @author fghpdf
 * @date 2020/6/2
 * @link https://leetcode.com/problems/intersection-of-two-arrays/
 **/
public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<>(16);
        Set<Integer> result = new HashSet<>();

        for (int value : nums1) {
            map.put(value, map.getOrDefault(value, 0) + 1);
        }

        for (int value : nums2) {
            if (map.get(value) != null && map.get(value) > 0) {
                result.add(value);
                map.put(value, map.get(value) - 1);
            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
