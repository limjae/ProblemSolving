package BinarySerch.프로그래머스_입국심사;

import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Long max = Integer.toUnsignedLong(Arrays.stream(times).max().getAsInt()) * Math.floorDiv(n, times.length);
        Long min = Integer.toUnsignedLong(Arrays.stream(times).min().getAsInt()) * Math.floorDiv(n, times.length);
        System.out.println(min);
        System.out.println(max);

        Boolean[] visited = new Boolean[n];
        while (min < max){
            Long mid = Math.floorDiv(min+max, 2);
            Long passedPeople = getPassAvailable(mid, times);
            if(passedPeople < n){
                min = mid + 1;
            }
            else {
                max = mid;
            }
        }
        return min;
    }

    public Long getPassAvailable(Long timePassed, int[] times){
        long passedPeople = 0L;
        for(int time : times){
            passedPeople += Math.floorDiv(timePassed, time);
        }
        return passedPeople;
    }
}