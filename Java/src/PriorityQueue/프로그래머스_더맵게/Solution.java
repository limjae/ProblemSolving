package PriorityQueue.프로그래머스_더맵게;

import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> scovilleHeap = new PriorityQueue<>();
        for(int value : scoville){
            scovilleHeap.add(value);
        }

        int mixTime = 0;
        while(!scovilleHeap.isEmpty() && scovilleHeap.peek() < K){
            if (scovilleHeap.size() < 2){
                return -1;
            }
            else {
                int firstDish = scovilleHeap.poll();
                int secondDish = scovilleHeap.poll();
                scovilleHeap.add(firstDish + 2 * secondDish);
                mixTime += 1;
            }
        }

        return mixTime;
    }
}
