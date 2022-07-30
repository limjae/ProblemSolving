package BruteForce.프로그래머스_모의고사;

import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[][] studentPattern = {
                {1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        int[] studentScores = {0, 0, 0};
        List<Integer> highestStudent = new ArrayList<>();

        for (int i = 0; i < answers.length; i++) {
            int answer = answers[i];

            studentScores[0] = answer == studentPattern[0][i%studentPattern[0].length] ?
                    studentScores[0] + 1 : studentScores[0];

            studentScores[1] = answer == studentPattern[1][i%studentPattern[1].length] ?
                    studentScores[1] + 1 : studentScores[1];

            studentScores[2] = answer == studentPattern[2][i%studentPattern[2].length] ?
                    studentScores[2] + 1 : studentScores[2];
        }
        OptionalInt maxScore = Arrays.stream(studentScores).max();

        for(int i = 0; i < studentScores.length; i++){
            if (studentScores[i] == maxScore.getAsInt()){
                highestStudent.add(i+1);
            }
        }

        return highestStudent.stream().mapToInt(Integer::intValue).toArray();
    }
}