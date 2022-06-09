package DynamicProgramming.boj_11054_mostLongestBitonicSubsequence;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int totalNumber;
    static int[] arr;
    static int[] dpIncrease;
    static int[] dpDecrease;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        totalNumber = Integer.parseInt(st.nextToken());
        arr = new int[totalNumber];
        dpIncrease = new int[totalNumber];
        dpDecrease = new int[totalNumber];

        st = new StringTokenizer(br.readLine());
        for (int i =0 ; i< totalNumber; ++i) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i < totalNumber; i++) {
            dpIncrease[i] = 1;
            for(int j = 0; j < i; j++) {
                if(arr[j] < arr[i] ) {
                    dpIncrease[i] = Math.max(dpIncrease[i] , dpIncrease[j] + 1);
                }
            }
        }

        for(int i = totalNumber-1; i > -1; i--) {
            dpDecrease[i] = 1;
            for(int j = totalNumber-1; j > i; j--) {
                if(arr[j] < arr[i] ) {
                    dpDecrease[i] = Math.max(dpDecrease[i] , dpDecrease[j] + 1);
                }
            }
        }

        int max = 0;
        for(int i = 0; i < totalNumber; i++){
            max = Math.max(max, dpDecrease[i]+dpIncrease[i]);
        }

        System.out.println(max-1);

    }
}
