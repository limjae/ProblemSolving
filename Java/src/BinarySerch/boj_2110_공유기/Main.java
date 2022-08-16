package BinarySerch.boj_2110_공유기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] option = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int houseSize = option[0];
        int switchSize = option[1];
        List<Integer> datas = new ArrayList<>();

        for (int i = 0; i < houseSize; ++i) {
            datas.add(Integer.valueOf(br.readLine()));
        }
        datas.sort(Comparator.naturalOrder());

        int left = 1;
        int right = datas.get(datas.size() - 1);
        while (left <= right) {

            int mid = (left + right) / 2;
//            System.out.println("mid = " + mid);
            int prev = datas.get(0);
            int count = 1;
            for (int i = 0; i < datas.size(); ++i) {
                if(datas.get(i) - prev >= mid){
                    count += 1;
                    prev = datas.get(i);
                }
            }

            if(count >= switchSize){
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }

        }

        System.out.println(right);
    }
}
