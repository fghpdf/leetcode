package OddEvenLinkedList;

import com.fghpdf.ListNode;

/**
 * @author fghpdf
 * @date 2020/01/01
 * @link https://leetcode.com/problems/odd-even-linked-list
 * the problem donnot care the value in node, it just want to group odd even nodes by number.
 * so it must first node is odd, second is even.
 **/
public class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head != null) {

            ListNode odd = head;
            ListNode even = head.next;
            ListNode evenHead = even;

            while (even != null && even.next != null) {
                odd.next = odd.next.next;
                even.next = even.next.next;
                odd = odd.next;
                even = even.next;
            }
            odd.next = evenHead;
        }
        return head;
    }
}
