package PriorityQueue.프로그래머스_디스크컨트롤러;

import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int currentTime = 0;
        PriorityQueue<Task> pq = new PriorityQueue<>();
        PriorityQueue<ReadyTask> readyPq = new PriorityQueue<>();

        for(int[] task : jobs){
            pq.add(new Task(task[0], task[1]));
        }

        while(!pq.isEmpty() || !readyPq.isEmpty()){
            while(!pq.isEmpty()){
                Task ready = pq.poll();
                if(ready.inTime <= currentTime){
                    readyPq.add(new ReadyTask(ready.inTime, ready.duration));
                }
                else{
                    pq.add(ready);
                    break;
                }
            }

            if(readyPq.isEmpty()){
                currentTime += 1;
            }
            else{
                ReadyTask run = readyPq.poll();
                answer += currentTime - run.inTime + run.duration;
                currentTime += run.duration;
            }
        }

        return Math.floorDiv(answer,jobs.length);
    }


}

class Task implements Comparable<Task>{
    public Integer inTime;
    public Integer duration;

    public Task(Integer inTime, Integer duration){
        this.inTime = inTime;
        this.duration = duration;
    }

    public Integer getTime(){
        return this.inTime;
    }

    @Override
    public int compareTo(Task b){
        return this.inTime - b.inTime;
    }

}

class ReadyTask implements Comparable<ReadyTask>{
    public Integer inTime;
    public Integer duration;

    public ReadyTask(Integer inTime, Integer duration){
        this.inTime = inTime;
        this.duration = duration;
    }

    @Override
    public int compareTo(ReadyTask b){
        return this.duration - b.duration;
    }

}