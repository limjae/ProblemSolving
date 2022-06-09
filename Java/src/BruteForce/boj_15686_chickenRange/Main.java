package BruteForce.boj_15686_chickenRange;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static class Location {
        int x, y;

        public Location(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
    static int answer = Integer.MAX_VALUE;
    static int mapSize = 0;
    static int aliveSize = 0;
    static ArrayList<Location> chickenList = new ArrayList<Location>();
    static Stack<Location> aliveList = new Stack<Location>();
    static ArrayList<Location> manList = new ArrayList<Location>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        mapSize = Integer.parseInt(st.nextToken());
        aliveSize = Integer.parseInt(st.nextToken());

        for (int indexY = 0; indexY < mapSize; ++indexY) {
            st = new StringTokenizer(br.readLine());
            for (int indexX = 0; indexX < mapSize; ++indexX) {
                int data = Integer.parseInt(st.nextToken());
                if (data == 1) {
                    manList.add(new Location(indexY, indexX));
                } else if (data == 2) {
                    chickenList.add(new Location(indexY, indexX));
                }
            }
        }
        combineChicken(0);
        System.out.println(answer);

    }

    public static void combineChicken(int curIndex) {
        if (aliveList.size() == aliveSize) {
            int chickenRange = 0;
            for (Location house: manList){
                int minRange = Integer.MAX_VALUE;
                for (Location chick: aliveList){
                    minRange = Math.min(minRange, Math.abs(house.x - chick.x) + Math.abs(house.y - chick.y));
                }
                chickenRange += minRange;
            }
            answer = Math.min(answer, chickenRange);
        }
        else if(curIndex < chickenList.size()) {
            for (int index = curIndex; index < chickenList.size()-(aliveSize - aliveList.size() -1); ++index) {
                aliveList.push(chickenList.get(index));
                combineChicken(index + 1);
                aliveList.pop();
            }
        }
    }
}
