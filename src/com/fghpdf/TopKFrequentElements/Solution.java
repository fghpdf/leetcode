package TopKFrequentElements;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2019/01/05
 * @link https://leetcode.com/problems/top-k-frequent-elements/
 * first get repeat times of all element
 * and then put these times into a bucket
 */
public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        List<Integer>[] bucket = new List[nums.length + 1];
        Map<Integer, Integer> times = new HashMap<>(nums.length);

        for (int num : nums) {
            times.put(num, times.getOrDefault(num, 0) + 1);
        }

        for (int num : times.keySet()) {
            int repeatTimes = times.get(num);
            if (bucket[repeatTimes] == null) {
                bucket[repeatTimes] = new ArrayList<>();
            }
            bucket[repeatTimes].add(num);
        }
        
        List<Integer> result = new ArrayList<>();
        for (int i = bucket.length - 1; i >= 0 && result.size() < k; i--) {
            if (bucket[i] != null) {
                result.addAll(bucket[i]);
            }
        }
        return result;
    }
}
