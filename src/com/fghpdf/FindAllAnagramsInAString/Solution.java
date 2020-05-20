package com.fghpdf.FindAllAnagramsInAString;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2020/5/20
 * @link https://leetcode.com/problems/find-all-anagrams-in-a-string/
 * just change the valid judge condition from sliding template
 **/
public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        // counter for needing character times
        Map<Character, Integer> need = new HashMap<>(p.length());
        // counter for character's times in window
        Map<Character, Integer> window = new HashMap<>(p.length());

        List<Integer> result = new LinkedList<>();

        // init
        for (char needChar : p.toCharArray()) {
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
        while(right < s.length()) {
            // will move in char
            char moveInChar = s.charAt(right);
            // extend
            right++;
            // update window
            if (need.containsKey(moveInChar)) {
                window.merge(moveInChar, 1, Integer::sum);
                if (need.get(moveInChar).equals(window.get(moveInChar))) {
                    valid++;
                }
            }

            while (right - left >= p.length()) {
                // will move out char
                char moveOutChar = s.charAt(left);
                // result
                if (valid == need.size()) {
                    result.add(left);
                }
                // shrink
                left++;
                // update window
                if (need.containsKey(moveOutChar)) {
                    if (need.get(moveOutChar).equals(window.get(moveOutChar))) {
                        valid--;
                    }
                    window.merge(moveOutChar, - 1, Integer::sum);
                }
            }

        }

        return result;
    }
}
