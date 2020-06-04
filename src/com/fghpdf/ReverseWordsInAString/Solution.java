package com.fghpdf.ReverseWordsInAString;

/**
 * @author fghpdf
 * @date 2020/6/4
 * @link https://leetcode.com/problems/reverse-words-in-a-string/
 **/
public class Solution {
    public String reverseWords(String s) {
        char[] sentence = s.trim().toCharArray();
        // step 1
        // reverse all string
        reverseInRange(sentence, 0, sentence.length - 1);

        // step 2
        // reverse words
        int wordStart = 0;
        for (int i = 0; i < sentence.length; i++) {
            if (sentence[i] == ' '){
                reverseInRange(sentence, wordStart, i - 1);
                // space
                wordStart = i + 1;
            }
        }

        // last word
        reverseInRange(sentence, wordStart, sentence.length - 1);

        return String.valueOf(sentence).trim();
    }

    private String fixWords(String s) {
        String[] words = s.trim().split("\\s");
        StringBuilder sb = new StringBuilder();
        for(int i = words.length-1; i>=0;i--){
            if(!words[i].trim().isEmpty()){
                sb.append(words[i]).append(" ");
            }
        }
        return sb.toString().trim();
    }

    private void reverseInRange(char[] s, int start, int end) {
        if (start >= end || s.length == 0) {
            return;
        }

        while (start < end) {
            // swap
            char temp = s[start];
            s[start] = s[end];
            s[end] = temp;

            // shrink
            start++;
            end--;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.reverseWords("the sky is blue");
    }
}
