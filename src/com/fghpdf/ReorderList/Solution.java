package com.fghpdf.ReorderList;

import com.fghpdf.ListNode;

/**
 * @author qxx
 * @date 10/15/2020
 * @link https://leetcode.com/problems/reorder-list/
 **/
public class Solution {
    public void reorderList(ListNode head) {
        if (head == null) {
            return;
        }
        // fast and slow find middle point
        ListNode fast = head;
        ListNode slow = head;

        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        // slow is 2 -> 3 -> 4 so should get next 3 -> 4
        ListNode middle = slow.next;

        // reverse right list
        ListNode right = reverseList(middle);
        // make head 1 -> 2 -> 3 to 1 -> 2 -> end
        slow.next = null;

        while (head != null && right != null) {
            ListNode temp = right.next;
            right.next = head.next;
            head.next = right;
            head = right.next;
            right = temp;
        }
    }

    private ListNode reverseList(ListNode head) {
        ListNode prev = null;

        while (head != null) {
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }

        return prev;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        Solution sol = new Solution();
        sol.reorderList(head);

        head.printlist(head);
    }
}
