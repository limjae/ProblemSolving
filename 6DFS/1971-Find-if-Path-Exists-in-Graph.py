from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination or n == 1:
            return True

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        path = set([source])
        stack = [source]
        while stack:
            cur_node = stack.pop()

            for link in graph[cur_node]:
                if destination == link:
                    return True
                elif path in path:
                    continue
                else:
                    path.add(path)
                    stack.append(link)

        return False


from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination or n == 1:
            return True

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        path = set()


        def DFS(cur_node):
            path.add(cur_node)

            for link in graph[cur_node]:
                if link in path:
                    continue
                elif link == destination:
                    return True
                elif DFS(link):
                    return True

            path.remove(cur_node)
            return False

        if DFS(source):
            return True
        return False
