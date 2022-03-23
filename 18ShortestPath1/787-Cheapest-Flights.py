# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# dijkstra 미해결
import copy
from typing import *
import heapq
# dijkstra
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, k + 1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w + dw, y, k - 1))
        return -1


# ballmanford
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [9999999] * n
        cost[src] = 0

        for i in range(k+1):
            temp = copy.copy(cost)
            for s, d, w in flights:
                if cost[s] == 9999999:
                    continue
                temp[d] = min(temp[d], cost[s] + w)
            cost = temp

        return cost[dst] if cost[dst] != 9999999 else -1



    # public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K)
    # {
    #     int[] cost=new int[n];
    #     Arrays.fill(cost,Integer.MAX_VALUE);
    #     cost[src]=0;
    #     for(int i=0;i<=K;i++)
    #     {
    #         int[] temp= Arrays.copyOf(cost,n);
    #         for(int[] f: flights)
    #         {
    #             int curr=f[0],next=f[1],price=f[2];
    #             if(cost[curr]==Integer.MAX_VALUE)
    #                 continue;
    #             temp[next]=Math.min(temp[next],cost[curr]+price);
    #         }
    #         cost=temp;
    #     }
    #     return cost[dst]==Integer.MAX_VALUE?-1:cost[dst];
    # }