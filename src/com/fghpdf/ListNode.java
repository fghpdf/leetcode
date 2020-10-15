package com.fghpdf;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) {
        val = x;
    }
    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public void printlist(ListNode node) {
        if (node == null) {
            return;
        }
        while (node != null) {
            System.out.print(node.val + " -> ");
            node = node.next;
        }
        System.out.println("end");
    }
}
