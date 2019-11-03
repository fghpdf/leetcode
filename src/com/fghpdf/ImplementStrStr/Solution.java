package com.fghpdf.ImplementStrStr;

public class Solution {
    public int strStr(String haystack, String needle) {
//        return haystack.indexOf(needle);
        if (needle.length() == 0) {
            return 0;
        }
        if (haystack.length() == 0) {
            return -1;
        }

        for (int i = 0; i < haystack.length(); i++) {
            if (i + needle.length() > haystack.length()) {
                break;
            }
            for (int j = 0; j < needle.length(); j++) {
                if (haystack.charAt(i + j) != needle.charAt(j)) {
                    break;
                }

                if (j == needle.length() - 1) {
                    return i;
                }
            }
        }
        return -1;
    }
}
