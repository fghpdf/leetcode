package com.fghpdf.LinkedListCycleII;

import com.fghpdf.ListNode;

/**
 * @author fghpdf
 * @date 2020/6/2
 * @link https://leetcode.com/problems/linked-list-cycle-ii/
 **/
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode runner = head;
        ListNode walker = head;

        boolean isCycle = false;

        // runner includes walker
        while (runner.next != null && runner.next.next != null) {
            walker = walker.next;
            runner = runner.next.next;
            if (runner == walker) {
                isCycle = true;
                break;
            }
        }

        if (!isCycle) {
            return null;
        }

        // twice will meet in enter point
        ListNode start = head;
        while(start != walker) {
            start = start.next;
            walker = walker.next;
        }


        return start;
    }
}
