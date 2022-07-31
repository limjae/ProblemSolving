package PriorityQueue.프로그래머스_가장큰수;

import java.util.*;
import java.util.stream.*;
class Solution {
    public String solution(int[] numbers) {
        StringBuilder answer = new StringBuilder();
        List<String> sortedNumbers = Arrays.stream(numbers)
                .mapToObj(i -> Integer.toString(i)+Integer.toString(i)+Integer.toString(i)+Integer.toString(i))
                .sorted()
                .collect(Collectors.toList());

        if(sortedNumbers.get(sortedNumbers.size() - 1).equals("0000")){
            return "0";
        }

        for(int i = sortedNumbers.size() - 1; i > -1; --i){
            String biggest = sortedNumbers.get(i);
            String orignalString = biggest.substring(0, biggest.length()/4);
            answer.append(orignalString);
        }

        return answer.toString();
    }
}