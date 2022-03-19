# https://leetcode.com/problems/reconstruct-itinerary/submissions/
from typing import *
from collections import defaultdict
from collections import deque

# 140~160ms
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airlines = defaultdict(list)
        tickets_count = len(tickets)
        # JFK = begin
        answer = ["JFK"]

        for ticket in sorted(tickets,key=lambda x:(x[1])):
            # from_air = ticket[0]
            # to_air = ticket[1]
            airlines[ticket[0]].append(ticket[1])

        def DFS(ticket_left, from_airport):
            if ticket_left == 0:
                return 1
            else:
                for i in range(len(airlines[from_airport])):
                    next = airlines[from_airport].pop(i)
                    answer.append(next)
                    if DFS(ticket_left-1, next):
                        return 1
                    else:
                        airlines[from_airport].insert(i, next)
                        answer.pop()
                return 0

        # JFK = begin
        DFS(tickets_count, "JFK")
        return answer

# 85~141ms
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airlines = defaultdict(list)
        # JFK = begin
        answer = ["JFK"]

        for ticket in sorted(tickets):
            # from_air = ticket[0]
            # to_air = ticket[1]
            # [ to_airport, is_used ]
            airlines[ticket[0]].append([ticket[1], False])

        def DFS(ticket_left, from_airport):
            if ticket_left == 0:
                return 1
            else:
                for i, ticket in enumerate(airlines[from_airport]):
                    if ticket[1]:
                        continue

                    next = ticket[0]
                    ticket[1] = True

                    answer.append(next)
                    if DFS(ticket_left - 1, next):
                        return 1
                    else:
                        ticket[1] = False
                        answer.pop()
                return 0

        # JFK = begin
        DFS(len(tickets), "JFK")
        return answer



# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] 주의

# 85~141ms
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airlines = defaultdict(set)

        ticket_count = len(tickets)
        for ticket in sorted(tickets):
            airlines[ticket[0]].add(ticket[1])

        queue = deque()
        queue.append("JFK")
        while queue:
            path = queue.popleft()
            if len(path) == ticket_count:
                return path
            else:
                for i, path_to in enumerate(airlines[path[-1]]):
                    queue.append(path + [path_to])

        return False
