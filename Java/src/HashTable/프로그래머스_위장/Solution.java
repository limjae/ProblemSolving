package HashTable.프로그래머스_위장;

import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;

        Map<String, Set<String>> closet = new HashMap<>();

        for(String[] cloth : clothes){
            Set<String> clothSet = closet.getOrDefault(cloth[1], new HashSet<>());
            clothSet.add(cloth[0]);
            closet.put(cloth[1], clothSet);
        }

        for(String clothType : closet.keySet()){
            Set<String> clothSet = closet.getOrDefault(clothType, new HashSet<>());
            answer *= (clothSet.size() + 1);
        }

        return answer - 1;
    }
}