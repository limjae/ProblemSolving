package Sorting.프로그래머스_전화번호부;

import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);

        for(int i = 0; i< phone_book.length - 1; ++i){
            if (phone_book[i + 1].startsWith(phone_book[i])){
                return false;
            }
        }
        return true;
    }
}