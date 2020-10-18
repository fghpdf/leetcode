package com.fghpdf.AddTwoNumbersII;

import com.fghpdf.ListNode;

import java.util.Stack;

/**
 * @author qxx
 * @date 10/18/2020
 * @link https://leetcode.com/problems/add-two-numbers-ii/
 **/
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> addOne = new Stack<>();
        Stack<Integer> addTwo = new Stack<>();
        ListNode result = new ListNode(-1);
        ListNode dummy = result.next;

        while (l1 != null) {
            addOne.push(l1.val);
            l1 = l1.next;
        }

        while (l2 != null) {
            addTwo.push(l2.val);
            l2 = l2.next;
        }

        int carry = 0;
        while (!addOne.isEmpty() || !addTwo.isEmpty()) {
            int numberOne = addOne.isEmpty() ? 0 : addOne.pop();
            int numberTwo = addTwo.isEmpty() ? 0 : addTwo.pop();

            int sum = numberOne + numberTwo + carry;
            carry = sum / 10;

            ListNode add = new ListNode(sum % 10);
            add.next = dummy;
            result.next = add;
            dummy = add;
        }

        if (carry == 1) {
            ListNode add = new ListNode(1);
            add.next = dummy;
            result.next = add;
        }

        return result.next;
    }
}
