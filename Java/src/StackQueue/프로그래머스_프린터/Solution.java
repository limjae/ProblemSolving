package StackQueue.프로그래머스_프린터;

import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer[]> printQueue = new LinkedList<>();

        for(int index = 0; index < priorities.length; ++index){
            Integer[] currentTask = {priorities[index], index};
            printQueue.add(currentTask);
        }

        while(!printQueue.isEmpty()){
            int maxPriority = maxPriority(printQueue);
            Integer[] currentTask = printQueue.poll();
            //System.out.println(Arrays.toString(currentTask));

            if(currentTask[0] < maxPriority){
                printQueue.add(currentTask);
            }
            else{
                // System.out.println("out");
                answer += 1;
                if(currentTask[1] == location){
                    return answer;
                }
            }
        }

        return -1;
    }

    public int maxPriority(Queue<Integer[]> queue){
        int max = 0;
        for(Integer[] object : queue){
            if (max < object[0]){
                max = object[0];
            }
        }
        return max;
    }

}