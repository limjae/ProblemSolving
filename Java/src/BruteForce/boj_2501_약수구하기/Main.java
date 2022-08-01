package BruteForce.boj_2501_약수구하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int p = input[0];
        int target = input[1];
        int count = 0;

        for (int i = 1; i < p + 1; ++i) {
            if (p % i == 0) {
                count += 1;
                if(count == target){
                    System.out.println(i);
                    return;
                }
            }
        }

        System.out.println(0);
    }
}
