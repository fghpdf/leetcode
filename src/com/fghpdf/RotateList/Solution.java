package com.fghpdf.RotateList;

import com.fghpdf.ListNode;

import javax.swing.*;

/**
 * @author qxx
 * @date 10/16/2020
 * @link https://leetcode.com/problems/rotate-list/
 **/
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) {
            return head;
        }

        // get the length of list
        ListNode tail = head;
        int size = 1;
        while (tail.next != null) {
            tail = tail.next;
            size++;
        }

        // get the newHead
        // move after size - k % size th element to head
        ListNode prev = head;
        for (int i = size - k % size; i > 1; i--) {
            prev = prev.next;
        }

        tail.next = head;
        head = prev.next;
        prev.next = null;

        return head;
    }

    private ListNode rotate(ListNode head) {
        // find tail and prev tail element
        ListNode tail = head;
        ListNode prev = head;

        while (tail.next != null) {
            prev = tail;
            tail = tail.next;
        }

        // move tail to head
        prev.next = null;
        tail.next = head;
        return tail;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
//        head.next.next.next = new ListNode(4);
//        head.next.next.next.next = new ListNode(5);

        Solution solution = new Solution();
        ListNode haha = solution.rotateRight(head,
        2);

        haha.printlist(haha);
    }
}
