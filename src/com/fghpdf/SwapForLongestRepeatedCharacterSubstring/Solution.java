package com.fghpdf.SwapForLongestRepeatedCharacterSubstring;

import java.util.LinkedList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2020/5/27
 * @link https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
 **/
public class Solution {
    public int maxRepOpt1(String text) {
        // group by alpha
        List<Integer>[] group = new LinkedList[26];
        // init 26 letters
        for (int i = 0; i < 26; i++) {
            group[i] = new LinkedList<>();
        }
        // init group by
        // a: [0, 1, 2, 4, 5, 6]
        for (int i = 0; i < text.length(); i++) {
            group[text.charAt(i) - 'a'].add(i);
        }

        int res = 1;

        // loop letters
        for (int letter = 0; letter < 26; letter++) {
            int current = 1;
            int prev = 0;
            int maxLength = 0;
            for (int j = 1; j < group[letter].size(); j++) {
                // continuous
                if (group[letter].get(j - 1) + 1 == group[letter].get(j)) {
                    current++;
                } else {
                    // can swap then continuous
                    prev = group[letter].get(j-1) + 2 == group[letter].get(j) ? current : 0;
                    // re init current
                    current = 1;
                }
                maxLength = Math.max(maxLength, prev + current);
            }
            // can swap one element
            if (group[letter].size() > maxLength) {
                maxLength += 1;
            }
            res = Math.max(res, maxLength);
        }

        return res;
    }
}
