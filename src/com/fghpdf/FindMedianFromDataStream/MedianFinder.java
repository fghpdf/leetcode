package com.fghpdf.FindMedianFromDataStream;

import java.util.Collections;
import java.util.PriorityQueue;

/**
 * @author fghpdf
 * @date 2020/6/6
 * @link https://leetcode.com/problems/find-median-from-data-stream/
 **/
public class MedianFinder {
    private final PriorityQueue<Integer> min = new PriorityQueue<>(Collections.reverseOrder());
    private final PriorityQueue<Integer> max = new PriorityQueue<>();
    private boolean isEven = true;

    /** initialize your data structure here. */
    public MedianFinder() {

    }

    public void addNum(int num) {
        if (isEven) {
            // even to odd
            // max peek is min peek
            max.offer(num);
            min.offer(max.poll());
        } else {
            // odd to even
            min.offer(num);
            max.offer(min.poll());
        }

        isEven = !isEven;
    }

    public double findMedian() {
        // median is one of heap
        if (isEven) {
            return (min.peek() + max.peek()) / 2.0;
        } else {
            return min.peek();
        }
    }
}
