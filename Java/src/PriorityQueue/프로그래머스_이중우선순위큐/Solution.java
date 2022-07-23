package PriorityQueue.프로그래머스_이중우선순위큐;

import java.util.*;
import java.util.function.Function;

public class Solution {
    public int[] solution(String[] operations) {
        DoubleEndPriorityQueue dpq = new DoubleEndPriorityQueue();
        Arrays.stream(operations).forEach(ops -> {
            String[] op = ops.split(" ");
            dpq.run(op[0], Integer.parseInt(op[1]));
        });
        int[] answer = {dpq.run("P", 1), dpq.run("P", -1)};
        return answer;
    }
}

class DoubleEndPriorityQueue {
    private final PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    private final PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    private Integer minDeleteCount = 0;
    private Integer maxDeleteCount = 0;
    private Map<Integer, Integer> deletedCount = new HashMap<>();
    private Map<String, Function<Integer, Integer>> commands = new HashMap<>();

    public DoubleEndPriorityQueue() {
        commands.put("I", x -> {
            minHeap.add(x);
            maxHeap.add(x);
            return x;
        });

        commands.put("D", x -> {
            if (x > 0 && maxHeap.size() - minDeleteCount > 0) {
                Integer peek = maxHeap.poll();
                maxDeleteCount++;
                deletedCount.put(peek, deletedCount.getOrDefault(peek, 0) + 1);
                return peek;
            } else if (x < 0 && minHeap.size() - maxDeleteCount > 0) {
                Integer peek = minHeap.poll();
                minDeleteCount++;
                deletedCount.put(peek, deletedCount.getOrDefault(peek, 0) + 1);
                return peek;
            }
            return 0;
        });

        commands.put("P", x -> {
            if (x > 0 && maxHeap.size() - minDeleteCount > 0) {

                Integer peek = maxHeap.poll();
                while (deletedCount.getOrDefault(peek, 0) > 0) {
                    deletedCount.put(peek, deletedCount.getOrDefault(peek, 0) - 1);
                    minDeleteCount--;
                    peek = maxHeap.poll();
                }

                return peek;
            } else if (x < 0 && minHeap.size() - maxDeleteCount > 0) {

                Integer peek = minHeap.poll();
                while (deletedCount.getOrDefault(peek, 0) > 0) {
                    deletedCount.put(peek, deletedCount.getOrDefault(peek, 0) - 1);
                    maxDeleteCount--;
                    peek = minHeap.poll();
                }

                return peek;
            }
            return 0;
        });
    }

    public Integer run(String command, Integer value) {
        return commands.get(command).apply(value);
    }
}