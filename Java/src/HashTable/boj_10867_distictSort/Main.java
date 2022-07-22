package HashTable.boj_10867_distictSort;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int lines = Integer.parseInt(br.readLine());

        String[] numbers = br.readLine().split(" ");

        int[] ints = Arrays.stream(numbers).mapToInt(Integer::parseInt).distinct().sorted().toArray();
        System.out.println(String.join(" ",Arrays.stream(ints).mapToObj(Integer::toString).toArray(String[]::new)));

    }
}