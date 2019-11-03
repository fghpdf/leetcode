package com.fghpdf.RomanToInterger;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    private Map<String, Integer> subtract = new HashMap<String, Integer>();
    private final String canSubStr = "IXC";
    private Map<String, Integer> alone = new HashMap<String, Integer>();

    public Solution() {
        subtract.put("IV", 4);
        subtract.put("IX", 9);
        subtract.put("XL", 40);
        subtract.put("XC", 90);
        subtract.put("CD", 400);
        subtract.put("CM", 900);

        alone.put("I", 1);
        alone.put("V", 5);
        alone.put("X", 10);
        alone.put("L", 50);
        alone.put("C", 100);
        alone.put("D", 500);
        alone.put("M", 1000);
    }


    public int romanToInt(String s) {
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (canSubStr.indexOf(c) != -1 && i != s.length() - 1) {
                String key = s.substring(i, i + 2);
                if (subtract.containsKey(key)) {
                    result += subtract.get(key);
                    i++;
                    continue;
                }
            }

            if (alone.containsKey(c + "")) {
                result += alone.get(c + "");
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.romanToInt("MCMXCIV"));
    }
}
