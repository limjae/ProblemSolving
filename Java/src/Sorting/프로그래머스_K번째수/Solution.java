package Sorting.프로그래머스_K번째수;

import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int index = 0; index < commands.length; ++index){
            int[] command = commands[index];
            int from = command[0] - 1;
            int to = command[1];
            int where = command[2] - 1;
            int[] splitArray = new int[to - from];

            if (to - from >= 0)
                System.arraycopy(array, from, splitArray, 0, to - from);
            Arrays.sort(splitArray);
            answer[index] = splitArray[where];
        }
        return answer;
    }
}