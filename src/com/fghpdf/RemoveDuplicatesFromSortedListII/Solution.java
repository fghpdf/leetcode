package com.fghpdf.RemoveDuplicatesFromSortedListII;

import com.fghpdf.ListNode;

/**
 * @author fghpdf
 * @date 2020/7/2
 * @link https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
 **/
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null||head.next==null) return head;

        if(head.val!=head.next.val){
            head.next=deleteDuplicates(head.next);
            return head;
        }
        else{
            while(head.next!=null&&head.val==head.next.val)
                head=head.next;

            return   deleteDuplicates(head.next);
        }

    }
}
