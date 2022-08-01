package GraphBFSDFS.boj_14888_연산자끼워넣기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int[] input;
    static int[] opCount;
    static int maxDFS = Integer.MIN_VALUE;
    static int minDFS = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(br.readLine());

        input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        opCount = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        DFS(1, input[0]);

        System.out.println(maxDFS);
        System.out.println(minDFS);
    }

    private static void DFS(int currentIndex, int value){
        if(currentIndex == input.length){
            maxDFS = Math.max(maxDFS, value);
            minDFS = Math.min(minDFS, value);
        }
        else {
            if(opCount[0] > 0){
                opCount[0] -= 1;
                DFS(currentIndex + 1, value + input[currentIndex]);
                opCount[0] += 1;
            }
            if(opCount[1] > 0){
                opCount[1] -= 1;
                DFS(currentIndex + 1, value - input[currentIndex]);
                opCount[1] += 1;
            }
            if(opCount[2] > 0){
                opCount[2] -= 1;
                DFS(currentIndex + 1, value * input[currentIndex]);
                opCount[2] += 1;
            }
            if(opCount[3] > 0){
                opCount[3] -= 1;
                DFS(currentIndex + 1, value / input[currentIndex]);
                opCount[3] += 1;
            }
        }
    }
}
