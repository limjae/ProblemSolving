class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        cnt = 0

        stack = []

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '1':
                    continue

                cnt += 1
                stack.append((row, col))

                while stack:
                    tmp = stack.pop()
                    y, x = tmp
                    # 방문 표시
                    grid[y][x] = '0'

                    # 1. 북으로 갈 수 있는가?
                    if y > 0:
                        # 북쪽 탐색 후 섬이면 스택에 저장
                        if grid[y - 1][x] == '1':
                            stack.append((y - 1, x))
                    # 2. 서로 갈 수 있는가?
                    if x > 0:
                        # 서쪽 탐색 후 섬이면 스택에 저장
                        if grid[y][x - 1] == '1':
                            stack.append((y, x - 1))
                    # 3. 남으로 갈 수 있는가?
                    if y < rows - 1:
                        # 서쪽 탐색 후 섬이면 스택에 저장
                        if grid[y + 1][x] == '1':
                            stack.append((y + 1, x))
                    # 4. 동으로 갈 수 있는가?
                    if x < cols - 1:
                        # 서쪽 탐색 후 섬이면 스택에 저장
                        if grid[y][x + 1] == '1':
                            stack.append((y, x + 1))

            # 단, stack은 역순으로 출력(pop)이 이루어지므로 실질적인 탐색순서는 동 -> 남 -> 서 -> 북이 됨

            return cnt


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        rows, cols = len(grid), len(grid[0])
        cnt = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '1':
                    continue

                cnt += 1
                stack = [(row, col)]

                while stack:
                    x, y = stack.pop()
                    grid[x][y] = '0'
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                            continue
                        stack.append((nx, ny))
        return cnt




