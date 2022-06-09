package DynamicProgramming.boj_11055_mostLargestIncreasingSubsequence;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int totalNumber;
    static int[] arr;
    static int[] dpSum;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        totalNumber = Integer.parseInt(st.nextToken());
        arr = new int[totalNumber];
        dpSum = new int[totalNumber];

        st = new StringTokenizer(br.readLine());
        for (int i =0 ; i< totalNumber; ++i){
            arr[i] = Integer.parseInt(st.nextToken());
        }


        int max = 0;
        for(int i = 0; i < totalNumber; i++) {
            dpSum[i] = arr[i];
            for(int j = 0; j < i; j++) {
                if(arr[j] < arr[i] ) {
                    dpSum[i] = Math.max(dpSum[i] , dpSum[j] + arr[i]);
                }
            }
            max = Math.max(dpSum[i], max);
        }

        System.out.println(max);

    }
}
