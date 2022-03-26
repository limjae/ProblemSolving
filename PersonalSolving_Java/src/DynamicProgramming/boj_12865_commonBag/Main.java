//https://www.acmicpc.net/problem/12865
package DynamicProgramming.boj_12865_commonBag;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static class pack {
        int weight, value;
        public pack(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }

    static int itemLength = 0;
    static int bagCapacity = 0;
    static ArrayList<pack> packList = new ArrayList<pack>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        itemLength = Integer.parseInt(st.nextToken());
        bagCapacity = Integer.parseInt(st.nextToken());

        for (int i = 0; i < itemLength; ++i) {
            st = new StringTokenizer(br.readLine());
            int inputWeight = Integer.parseInt(st.nextToken());
            int inputValue = Integer.parseInt(st.nextToken());
            packList.add(new pack(inputWeight, inputValue));
        }
        System.out.println(knapsack());
    }

    public static int knapsack() {
        int[][] dp = new int [itemLength + 1][bagCapacity + 1];
        for (int i=0; i< itemLength + 1; ++i) {
            for(int j=0; j< bagCapacity+1;++j){
                if(i ==0 || j == 0) {
                    continue;
                }
                else if(j >= packList.get(i-1).weight) {
                    dp[i][j] = Math.max(packList.get(i-1).value + dp[i-1][j - packList.get(i-1).weight], dp[i-1][j]);
                }
                else {
                    dp[i][j] = dp[i-1][j];
                }

            }
        }

        return dp[itemLength][bagCapacity];
    }

}


