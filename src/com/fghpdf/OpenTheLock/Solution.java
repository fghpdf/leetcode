package com.fghpdf.OpenTheLock;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

/**
 * @author fghpdf
 * @date 2020/5/20
 * @link https://leetcode.com/problems/open-the-lock/
 **/
public class Solution {
    public int openLock(String[] deadends, String target) {
        // wait for handling
        Queue<String> needHandle = new LinkedList<>();
        // avoid for repeating
        Set<String> visited = new HashSet<>();

        // init
        int step = 0;
        // add first element
        needHandle.offer("0000");
        visited.add("0000");

        // deadends can't be visited
        for (String deadend : deadends) {
            visited.add(deadend);
            if ("0000".equals(deadend)) {
                return -1;
            }
        }

        while (!needHandle.isEmpty()) {
            int needHandleNums = needHandle.size();

            // extend for around
            for (int i = 0; i < needHandleNums; i++) {
                String current = needHandle.poll();

                if (current == null) {
                    continue;
                }

                // judge
                if (target.equals(current)) {
                    return step;
                }

                // add unvisited element to queue
                for (int slot = 0; slot < 4; slot++) {
                    // up
                    String up = upOperation(current, slot);
                    if (!visited.contains(up)) {
                        needHandle.add(up);
                        visited.add(up);
                    }

                    // down
                    String down = downOperation(current, slot);
                    if (!visited.contains(down)) {
                        needHandle.add(down);
                        visited.add(down);
                    }
                }
            }

            step++;
        }
        return -1;
    }

    /**
     * up operation for one slot in wheels
     * @param s String
     * @param slot int
     */
    private String upOperation(String s, int slot) {
        char[] wheels = s.toCharArray();
        if (wheels[slot] == '9') {
            wheels[slot] = '0';
        } else {
            wheels[slot] += 1;
        }

        return new String(wheels);
    }

    /**
     * down operation for one slot in wheels
     * @param s String
     * @param slot int
     */
    private String downOperation(String s, int slot) {
        char[] wheels = s.toCharArray();
        if (wheels[slot] == '0') {
            wheels[slot] = '9';
        } else {
            wheels[slot] -= 1;
        }

        return new String(wheels);
    }

    public static void main(String[] args) {
        String[] deadends = new String[]{"0201","0101","0102","1212","2002"};
        Solution solution = new Solution();
        int res = solution.openLock(deadends, "0009");
        System.out.println(res);
    }
}
