package GraphBFSDFS.프로그래머스_게임맵최단거리;

import java.util.*;

class Solution {
    static int[] dy = {1, 0, -1, 0};
    static int[] dx = {0, 1, 0, -1};

    public int solution(int[][] maps) {
        int xLength = maps[0].length;
        int yLength = maps.length;


        Deque<Integer[]> searchQueue = new LinkedList<>();
        Integer[] first = {0, 0, 1};
        maps[0][0] = -1;
        searchQueue.add(first);

        //BFS
        while (!searchQueue.isEmpty()) {
            Integer[] curPoint = searchQueue.poll();
            int y = curPoint[0];
            int x = curPoint[1];
            int distance = curPoint[2];

            if (x == xLength - 1 && y == yLength - 1) {
                return distance;
            }

            for (int i = 0; i < 4; ++i) {
                if (y + dy[i] > -1 && y + dy[i] < yLength &&
                        x + dx[i] > -1 && x + dx[i] < xLength) {

                    if (maps[y + dy[i]][x + dx[i]] == 1) {
                        Integer[] next = {y + dy[i], x + dx[i], distance + 1};
                        maps[y + dy[i]][x + dx[i]] = -1;
                        searchQueue.add(next);
                    }

                }
            }

        }

        return -1;
    }
}
