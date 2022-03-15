# https://leetcode.com/problems/course-schedule/submissions/
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        directed_graph = defaultdict(list)
        for pre in prerequisites:
            # pre[0] = target
            # pre[1] = required
            directed_graph[pre[0]].append(pre[1])

        # 방문 기록 체크
        visited = [False for _ in range(numCourses)]
        # 탐색 완료 체크
        finished = [False for _ in range(numCourses)]

        def DFS(course):
            if finished[course]:
                return True

            # finished[course] == False인 경우만 동작
            if visited[course]:
                return False
            visited[course] = True

            for require in directed_graph[course]:
                if not DFS(require):
                    return False

            finished[course] = True
            return True

        for course_num in range(numCourses):
            if not DFS(course_num):
                return False
        return True





