package GraphBFSDFS.boj_1260_DFSBFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    private static boolean[] dfsVisited;
    static List<Integer> dfsPath = new ArrayList<>();
    static Map<Integer, List<Integer>> graph = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] options = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int vertexCount = options[0];
        int edgeCount = options[1];
        int start = options[2];

        for (int i = 0; i < edgeCount; i++) {
            int[] link = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            List<Integer> direction1 = graph.getOrDefault(link[0], new ArrayList<>());
            direction1.add(link[1]);
            graph.put(link[0], direction1);

            List<Integer> direction2 = graph.getOrDefault(link[1], new ArrayList<>());
            direction2.add(link[0]);
            graph.put(link[1], direction2);
        }

        graph.keySet().forEach(
                k -> {
                    graph.get(k).sort(Comparator.naturalOrder());
                }
        );

//        System.out.println("graph.toString() = " + graph.toString());

        //dfs
        dfsVisited = new boolean[vertexCount];
        Arrays.fill(dfsVisited, false);
        dfsVisited[start - 1] = true;
        DFS(start);

        System.out.println(dfsPath.stream().map(String::valueOf).collect(Collectors.joining(" ")));

        //bfs
        List<Integer> bfsPath = new ArrayList<>();
        boolean[] visited = new boolean[vertexCount];
        Arrays.fill(visited, false);
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start - 1] = true;

        while (!queue.isEmpty()) {
            int curNode = queue.poll();
            bfsPath.add(curNode);
            List<Integer> connected = graph.getOrDefault(curNode, new ArrayList<>());

            connected.forEach(i -> {
                if (!visited[i - 1]) {
                    queue.add(i);
                    visited[i - 1] = true;
                }
            });
        }

        System.out.println(bfsPath.stream().map(String::valueOf).collect(Collectors.joining(" ")));
    }

    public static void DFS(int curNode) {
        dfsPath.add(curNode);
        List<Integer> connected = graph.getOrDefault(curNode, new ArrayList<>());

        connected.forEach(i -> {
            if (!dfsVisited[i - 1]) {
                dfsVisited[i - 1] = true;
                DFS(i);
            }
        });
    }
}
