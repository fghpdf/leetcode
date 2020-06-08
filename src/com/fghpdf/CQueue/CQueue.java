package com.fghpdf.CQueue;

import java.util.Stack;

/**
 * @author fghpdf
 * @date 2020/6/8
 * @link https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
 **/
public class CQueue {
    private Stack<Integer> stackOne = new Stack<>();
    private Stack<Integer> stackTwo = new Stack<>();

    public CQueue() {

    }

    public void appendTail(int value) {
        // push use stack one
        stackOne.push(value);
    }

    public int deleteHead() {
        // pop use stack two from stack one
        if (!stackTwo.isEmpty()) {
            return stackTwo.pop();
        }

        if (stackOne.isEmpty()) {
            return -1;
        }

        while (!stackOne.isEmpty()) {
            stackTwo.push(stackOne.pop());
        }

        return stackTwo.pop();
    }
}
