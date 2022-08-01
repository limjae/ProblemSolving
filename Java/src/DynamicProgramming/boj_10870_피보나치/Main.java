package DynamicProgramming.boj_10870_피보나치;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer target = Integer.valueOf(br.readLine());

        Integer cur = 0;
        Integer next = 1;

        for(int i = 0; i< target; ++i){
            Integer fibo = cur + next;
            cur = next;
            next = fibo;
        }
        System.out.println(cur);
    }
}
