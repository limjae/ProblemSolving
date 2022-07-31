package StackQueue.boj_10828_Stack;
//https://www.acmicpc.net/problem/10828

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.function.Consumer;

public class Main {
    static private List<Integer> stack = new ArrayList<>();
    static private Map<String, Consumer<Integer>> commands = new HashMap<>();

    public static void main(String[] args) throws IOException {
        commands.put("push", x -> {
            stack.add(x);
        });

        commands.put("pop", x -> {
            if(stack.size() > 0){
                System.out.println(stack.get(stack.size()-1));
                stack.remove(stack.size()-1);
            }
            else {
                System.out.println(-1);
            }
        });

        commands.put("top", x -> {
            if(stack.size() > 0){
                System.out.println(stack.get(stack.size()-1));
            }
            else {
                System.out.println(-1);
            }
        });

        commands.put("size", x -> {
            System.out.println(stack.size());
        });

        commands.put("empty", x -> {
            if(stack.isEmpty()){
                System.out.println(1);
            }
            else {
                System.out.println(0);
            }
        });


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int lines = Integer.parseInt(br.readLine());

        for (int i = 0; i < lines; i++) {
            String[] strings = br.readLine().split(" ");
            String command = strings[0];
//            null 을 허욜..?
            Integer arg = strings.length > 1 ? Integer.parseInt(strings[1]) : null;

            commands.get(command).accept(arg);

        }
    }
}

//14
//push 1
//push 2
//top
//size
//empty
//pop
//pop
//pop
//size
//empty
//pop
//push 3
//empty
//top