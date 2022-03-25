import sys
map_size = int(sys.stdin.readline())
normal_map = []
RG_map = []
normal_space = 0
RG_space = 0

for _ in range(map_size):
    data = sys.stdin.readline()[:-1]
    normal_map.append(list(data))
    data = data.replace("R", "A")
    data = data.replace("G", "A")
    RG_map.append(list(data))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for row in range(map_size):
    for col in range(map_size):
        if normal_map[row][col] != 'R':
            continue
        normal_space += 1
        stack = [(row, col)]

        while stack:
            x, y = stack.pop()
            normal_map[x][y] = '0'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size or normal_map[nx][ny] != 'R':
                    continue
                stack.append((nx, ny))

for row in range(map_size):
    for col in range(map_size):
        if normal_map[row][col] != 'G':
            continue
        normal_space += 1
        stack = [(row, col)]

        while stack:
            x, y = stack.pop()
            normal_map[x][y] = '0'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size or normal_map[nx][ny] != 'G':
                    continue
                stack.append((nx, ny))

for row in range(map_size):
    for col in range(map_size):
        if normal_map[row][col] != 'B':
            continue
        normal_space += 1
        stack = [(row, col)]

        while stack:
            x, y = stack.pop()
            normal_map[x][y] = '0'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size or normal_map[nx][ny] != 'B':
                    continue
                stack.append((nx, ny))

for row in range(map_size):
    for col in range(map_size):
        if RG_map[row][col] != 'A':
            continue
        RG_space += 1
        stack = [(row, col)]

        while stack:
            x, y = stack.pop()
            RG_map[x][y] = '0'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size or RG_map[nx][ny] != 'A':
                    continue
                stack.append((nx, ny))

for row in range(map_size):
    for col in range(map_size):
        if RG_map[row][col] != 'B':
            continue
        RG_space += 1
        stack = [(row, col)]

        while stack:
            x, y = stack.pop()
            RG_map[x][y] = '0'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size or RG_map[nx][ny] != 'B':
                    continue
                stack.append((nx, ny))


print(normal_space, RG_space)
