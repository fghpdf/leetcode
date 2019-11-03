package com.fghpdf.MergeTwoSortedLists;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode sortedList = new ListNode(0);
        ListNode head = sortedList;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                sortedList.next = l1;
                sortedList = sortedList.next;

                l1 = l1.next;
            } else {
                sortedList.next = l2;
                sortedList = sortedList.next;

                l2 = l2.next;
            }
        }

        if (l1 != null) {
            sortedList.next = l1;
        }

        if (l2 != null) {
            sortedList.next = l2;
        }

        return head.next;
    }

//    public static void main(String[] args) {
//        Solution sol = new Solution();
//
//        System.out.println(sol.mergeTwoLists());
//    }
}
