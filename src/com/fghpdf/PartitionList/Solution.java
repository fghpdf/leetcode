package com.fghpdf.PartitionList;

import com.fghpdf.ListNode;

/**
 * @author qxx
 * @date 10/17/2020
 * @link https://leetcode.com/problems/partition-list/
 **/
public class Solution {
    public ListNode partition(ListNode head, int x) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode small = new ListNode(-1);
        ListNode big = new ListNode(-1);
        ListNode smallHead = small;
        ListNode bigHead = big;

        while (head != null) {
            if (head.val >= x) {
                // join to big
                big.next = head;
                big = big.next;
            } else {
                // join to small
                small.next = head;
                small = small.next;
            }
            head = head.next;
        }

        // no cycle
        big.next = null;
        small.next = bigHead.next;

        return smallHead.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(4);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(2);
        head.next.next.next.next = new ListNode(5);
        head.next.next.next.next.next = new ListNode(2);

        Solution solution = new Solution();
        ListNode result =  solution.partition(head, 3);

        result.printlist(result);
    }
}
