package GraphBFSDFS;

import java.math.*;
import java.util.*;
import java.util.stream.*;

class Solution {

    public static int[] number;
    public static boolean[] combined;
    public static int answer = 0;
    public static Set<Integer> numberCombine = new HashSet<>();

    public int solution(String numbers) {
        number = Arrays.stream(numbers.split("")).mapToInt(Integer::valueOf).toArray();
        combined = new boolean[number.length];
        Arrays.fill(combined, false);
        Arrays.sort(number);

        //System.out.println(Arrays.toString(number));
        DFS(0);
        //System.out.println(numberCombine.toString());

        for(int combined : numberCombine){
            BigInteger b = new BigInteger(String.valueOf(combined));
            if(b.isProbablePrime(10)){
                answer += 1;
            }
        }
        return answer;
    }

    public void DFS(int curNumber){
        for(int i=0; i< number.length; ++i){
            if(combined[i] == false){
                combined[i] = true;
                DFS(curNumber);

                numberCombine.add(10 * curNumber + number[i]);
                DFS(10 * curNumber + number[i]);
                combined[i] = false;
            }
        }
    }

}