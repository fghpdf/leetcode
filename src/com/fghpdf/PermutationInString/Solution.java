package com.fghpdf.PermutationInString;

import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2020/5/19
 * @link https://leetcode.com/problems/permutation-in-string/
 * use sliding window template
 * the shrink condition is window length >= s1 length
 * the return condition is vaild == need size
 **/
public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // counter for needing character times
        Map<Character, Integer> need = new HashMap<>(s1.length());
        // counter for character times in window
        Map<Character, Integer> window = new HashMap<>(s2.length());

        // init
        for (char needChar : s1.toCharArray()) {
            need.merge(needChar, 1, Integer::sum);
            window.put(needChar, 0);
        }

        int left = 0, right = 0;
        // counter for how many Satisfy need condition in window
        // need times == times in window
        int valid = 0;

        // loop [left, right)
        // first extend window's right
        // then shrink window's left
        while (right < s2.length()) {
            // will move in window
            char moveInChar = s2.charAt(right);
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
            while (right - left >= s1.length()) {
                // Permutation exist
                if (valid == need.size()) {
                    return true;
                }

                // will move out of window
                char moveOutChar = s2.charAt(left);
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

        return false;
    }
}
