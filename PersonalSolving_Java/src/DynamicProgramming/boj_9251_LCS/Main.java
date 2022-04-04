package DynamicProgramming.boj_9251_LCS;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {

    static char[] s1;
    static char[] s2;
    static int l1;
    static int l2;
    static int[][] dp;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        s1 = br.readLine().toCharArray();
        s2 = br.readLine().toCharArray();
        l1 = s1.length;
        l2 = s2.length;

        dp = new int[l1 + 1][l2 + 1];

        for(int i = 1; i <= l1; i++) {
            for(int j = 1; j <= l2; j++) {
                if(s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }

                else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
//        System.out.println(Arrays.deepToString(dp));
        System.out.println(dp[l1][l2]);

    }

}