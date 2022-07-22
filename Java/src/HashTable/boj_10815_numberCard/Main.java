package HashTable.boj_10815_numberCard;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    static HashSet<Integer> cardSet = new HashSet<Integer>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int setLength = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i< setLength;++i){
            cardSet.add(Integer.parseInt(st.nextToken()));
        }

        int myLength = Integer.parseInt(br.readLine());
        st =new StringTokenizer(br.readLine());
        for(int i = 0; i< myLength;++i){
            if(cardSet.contains(Integer.parseInt(st.nextToken()))){
                System.out.print("1 ");
            }
            else{
                System.out.print("0 ");
            }
        }
    }
}
