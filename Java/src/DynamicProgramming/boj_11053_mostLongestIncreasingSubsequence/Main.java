package DynamicProgramming.boj_11053_mostLongestIncreasingSubsequence;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int totalNumber;
    static int[] arr;
    static int[] dpLength;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        totalNumber = Integer.parseInt(st.nextToken());
        arr = new int[totalNumber];
        dpLength = new int[totalNumber];

        st = new StringTokenizer(br.readLine());
        for (int i =0 ; i< totalNumber; ++i){
            arr[i] = Integer.parseInt(st.nextToken());
        }


        int max = 0;
        for(int i = 0; i < totalNumber; i++) {
            dpLength[i] = 1;
            for(int j = 0; j < i; j++) {
                if(arr[j] < arr[i] ) {
                    dpLength[i] = Math.max(dpLength[i] , dpLength[j] + 1);
                }
            }
            max = Math.max(dpLength[i], max);
        }

        System.out.println(max);

    }
}
