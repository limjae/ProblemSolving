package DynamicProgramming.프로그래머스_N으로표현;

import java.util.*;

class Solution {
    public int solution(int N, int number) {
        HashMap<Integer, Integer> calculationMap = new HashMap();
        int initNumber = N;
        for(int i = 1; i< 9;++i){
            calculationMap.put(initNumber, i);
            initNumber = 10 * initNumber + N;
        }

        for(int i=0; i< 8;++i){
            List<Integer> calculationSet = new ArrayList<>(calculationMap.keySet());
            for(Integer fromKey: calculationSet){
                for(Integer toKey: calculationSet){
                    Integer fromCount = calculationMap.get(fromKey);
                    Integer toCount = calculationMap.get(toKey);
                    if(fromCount + toCount < 9){
                        Integer destCount = calculationMap.getOrDefault(fromKey + toKey, 9);
                        calculationMap.put(fromKey+toKey, Math.min(fromCount + toCount, destCount));

                        destCount = calculationMap.getOrDefault(fromKey - toKey, 9);
                        calculationMap.put(fromKey-toKey, Math.min(fromCount + toCount, destCount));

                        destCount = calculationMap.getOrDefault(fromKey *toKey, 9);
                        calculationMap.put(fromKey*toKey, Math.min(fromCount + toCount, destCount));

                        if(toKey != 0){
                            destCount = calculationMap.getOrDefault(Math.floorDiv(fromKey,toKey), 9);
                            calculationMap.put(Math.floorDiv(fromKey,toKey), Math.min(fromCount + toCount, destCount));
                        }
                    }
                }
            }
        }

        return calculationMap.getOrDefault(number, -1);
    }


}