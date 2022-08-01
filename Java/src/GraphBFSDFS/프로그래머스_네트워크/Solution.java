package GraphBFSDFS.프로그래머스_네트워크;

import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        Arrays.fill(visited, false);

        for(int node = 0; node < n; ++node){
            if(visited[node] == false){
                answer += 1;

                Queue<Integer> queue = new LinkedList<>();
                queue.add(node);
                while(!queue.isEmpty()){
                    Integer curNode = queue.poll();
                    visited[curNode] = true;
                    for(int nextNode = 0; nextNode < n; ++nextNode){
                        if(computers[curNode][nextNode] == 1 && visited[nextNode] == false){
                            queue.add(nextNode);
                        }
                    }
                }

            }
        }
        return answer;
    }
}