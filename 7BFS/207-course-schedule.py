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
            visited[course] = True

            for require in directed_graph[course]:
                # 이미 탐색 완료했다면 넘어간다
                if finished[require]:
                    continue
                # 방문된 노드면 그 노드는 경로 상의 정점
                elif visited[require]:
                    return False

                # 반환된 값이 False면 순환 그래프 탐지
                if not DFS(require):
                    return False

            # 재귀가 끝나고 반환된다면 탐색을 완료 표시
            finished[course] = True
            return True

        for course_num in range(numCourses):
            if not visited[course_num] and not DFS(course_num):
                return False
        return True



