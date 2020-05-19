package com.fghpdf.MinimumWindowSubstring;

import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2020/5/19
 * @link https://leetcode.com/problems/minimum-window-substring/
 * need a window
 * first extend it to right until satisfy condition
 * and then shrink it from left to right until min length
 **/
public class Solution {
    public String minWindow(String s, String t) {
        // counter for needing character times
        Map<Character, Integer> need = new HashMap<>(t.length());
        // counter for character times in window
        Map<Character, Integer> window = new HashMap<>(t.length());

        // init need and window
        for (char needChar : t.toCharArray()) {
            need.merge(needChar, 1, Integer::sum);
            window.put(needChar, 0);
        }

        int left = 0;
        int right = 0;
        // counter for how many Satisfy need condition in window
        // need times == times in window
        int valid = 0;
        // init min sub character
        int minStart = 0;
        int minLength = Integer.MAX_VALUE;

        // loop [left, right)
        // first extend window's right
        // then shrink window's left
        while (right < s.length()) {
            // will move in window
            char moveInChar = s.charAt(right);
            // extend
            right++;
            // update window
            if (need.containsKey(moveInChar)) {
                // window[moveInChar]++;
                window.merge(moveInChar, 1, Integer::sum);
                if (window.get(moveInChar).equals(need.get(moveInChar))) {
                    valid++;
                }
            }

            // shrink window
            while (valid == need.size()) {
                // update min sub character
                if (minLength > right - left) {
                    minStart = left;
                    minLength = right - left;
                }

                // will move out of window
                char moveOutChar = s.charAt(left);
                // shrink
                left++;
                // update window
                if (need.containsKey(moveOutChar)) {
                    if (need.get(moveOutChar).equals(window.get(moveOutChar))) {
                        valid--;
                    }
                    window.merge(moveOutChar, -1, Integer::sum);
                }
            }
        }

        // return
        return minLength == Integer.MAX_VALUE ?
                "" : s.substring(minStart, minStart + minLength);
    }
}
