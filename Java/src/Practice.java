import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Practice {
    public static void main(String[] args) {
        solution("3");

    }

    public static void solution(String count) {
        int totalScore = 0;
        int countToInt = Integer.parseInt(count);


        for (int i = 0; i < countToInt; i++) {

            StringBuilder name = new StringBuilder("NT");
            int score = (int) (Math.random() * 100);
            String jobNumber = Integer.toString((int) (Math.random() * 100000));

            name.append("0".repeat(Math.max(0, 5 - jobNumber.length())));
            name.append(jobNumber);

            totalScore += score;
            System.out.println(name + " " + score);
        }

        double averageScore = (double) (totalScore / countToInt);
        System.out.println("생성된 점수의 평균은 = " + averageScore + "점입니다.");
    }
}
