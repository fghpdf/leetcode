package com.fghpdf.ConvertBinarySearchTreeToSortedDoublyLinkedList;

/**
 * @author fghpdf
 * @date 2020/6/15
 * @link https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
 **/
public class Solution {
    private Node prev, head;

    public Node treeToDoublyList(Node root) {
        if (root == null) {
            return null;
        }

        dfs(root);

        // tail connect head
        head.left = prev;
        prev.right = head;
        return head;
    }

    private void dfs(Node current) {
        if (current == null) {
            return;
        }

        // inorder
        // left
        dfs(current.left);

        // root
        // Doubly Linked List
        // prev.next = current
        // current.prev = prev
        if (prev != null) {
            prev.right = current;
        } else {
            head = current;
        }

        current.left = prev;

        // loop
        prev = current;

        dfs(current.right);
    }
}
