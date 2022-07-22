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

        System.out.println(String.join(" ",
                Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt).distinct().sorted()
                        .mapToObj(Integer::toString).toArray(String[]::new)));
    }
}