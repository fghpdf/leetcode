package com.fghpdf.SwapNodesInPairs;

import com.fghpdf.ListNode;

/**
 * @author qxx
 * @date 10/16/2020
 * @link https://leetcode.com/problems/swap-nodes-in-pairs/
 **/
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        // save pre element to connect
        ListNode pre = dummy;
        while (head != null && head.next != null) {
            // save second element
            ListNode second = head.next;
            // make the first element point third element head: 1 -> 3
            head.next = second.next;
            // make second element point first temp: 2 -> 1
            second.next = head;
            // make dummy/head point second element pre: 0 -> 2
            pre.next = second;
            // pre change to head actually is pre element pre: 1 -> 3
            pre = head;
            // head change to third head: 3 -> 4
            head = head.next;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);

        head.printlist(head);

        Solution sol = new Solution();
        sol.swapPairs(head);

        head.printlist(head);
    }
}
