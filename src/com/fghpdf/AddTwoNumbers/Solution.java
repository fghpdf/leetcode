package com.fghpdf.AddTwoNumbers;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import com.fghpdf.ListNode;

/**
 * @author fghpdf
 * @date 2019/11/8
 **/
public class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode result = new ListNode(0);
		ListNode resultHead = result;

		int sum = 0;
		while (l1 != null || l2 != null) {
			sum = sum / 10;

			if (l1 != null) {
				sum += l1.val;
				l1 = l1.next;
			}

			if (l2 != null) {
				sum += l2.val;
				l2 = l2.next;
			}

			resultHead.next = new ListNode(sum % 10);
			System.out.println(resultHead);
			System.out.println(resultHead.next);
			resultHead = resultHead.next;
			System.out.println(resultHead);
		}

		if (sum / 10 == 1) {
			resultHead.next = new ListNode(1);
		}

		return result.next;
	}
}
