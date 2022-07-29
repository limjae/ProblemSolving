package Stack.프로그래머스_기능개발;

import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> leftDaysQueue = new LinkedList<>();
        List<Integer> answer = new ArrayList<>();

        for(int i = 0; i< progresses.length; ++i){
            int leftDay = (int)Math.ceil((100 - progresses[i]) / (double)speeds[i]);

            leftDaysQueue.add(leftDay);
        }

        int dayPassed = 0;
        while(!leftDaysQueue.isEmpty()){
            int completedProgressCount = 0;
            while(!leftDaysQueue.isEmpty() && leftDaysQueue.peek() <= dayPassed){
                completedProgressCount += 1;
                leftDaysQueue.poll();
            }
            if (completedProgressCount > 0){
                answer.add(completedProgressCount);
            }
            dayPassed += 1;
        }

        List<Integer> integers = answer.stream().map(Integer::intValue).toList();
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}