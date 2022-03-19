# https://leetcode.com/problems/course-schedule/submissions/
from typing import *
from collections import defaultdict


# noinspection DuplicatedCode,PyPep8Naming

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        directed_graph = defaultdict(list)
        for pre in prerequisites:
            directed_graph[pre[0]].append(pre[1])

        visited = [False for _ in range(numCourses)]
        finished = [False for _ in range(numCourses)]

        def DFS(course):
            visited[course] = True

            for link in directed_graph[course]:
                if finished[link]:
                    continue
                elif visited[link]:
                    return False
                elif not DFS(link):
                    return False

            finished[course] = True
            return True

        for course_index in range(numCourses):
            if not visited[course_index] and not DFS(course_index):
                return False
        return True


solution = Solution()
solution.canFinish(2, [[0, 1], [1, 0]])