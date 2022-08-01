package BruteForce.boj_1292_쉽게푸는문제;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] table = new int[1001];

        int index = 0;
        int value = 1;

        while (index < 1001) {
            for (int i = 0; i < value; ++i) {
                ++index;
                if (index == 1001) {
                    break;
                }
                table[index] = value;
            }
            value++;
        }

        int a = input[0];
        int b = input[1];

        int answer = 0;

        for (int i = a; i < b + 1; ++i) {
            answer += table[i];
        }
        System.out.println(answer);
    }
}
