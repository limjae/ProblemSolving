package GraphBFSDFS.프로그래머스_타겟넘버;

import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        int goalIndex = numbers.length - 1;

        //List<index, value>
        Queue<List<Integer>> calculationQueue = new LinkedList<>();
        calculationQueue.add(new ArrayList<>(List.of(0,numbers[0])));
        calculationQueue.add(new ArrayList<>(List.of(0,-numbers[0])));

        //BFS
        while(!calculationQueue.isEmpty()){
            List<Integer> currentQueue = calculationQueue.poll();
            Integer currentIndex = currentQueue.get(0);
            Integer currentValue = currentQueue.get(1);

            if(currentIndex == goalIndex){
                if(currentValue == target){
                    answer += 1;
                }
            }
            else{
                Integer nextIndex = currentIndex + 1;
                Integer nextValuePlus = currentValue + numbers[nextIndex];
                Integer nextValueMinus = currentValue - numbers[nextIndex];

                calculationQueue.add(new ArrayList<>(List.of(nextIndex,nextValuePlus)));
                calculationQueue.add(new ArrayList<>(List.of(nextIndex,nextValueMinus)));
            }
        }


        return answer;
    }
}