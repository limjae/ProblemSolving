# https://www.acmicpc.net/problem/2667
# DFS로 해결

count = int(input())

house_map = []
visited_map = [[-1 for _ in range(count)] for _ in range(count)]
house_size = []

for _ in range(count):
    map_row = input()
    house_map.append([int(point) for point in map_row])


def DFS(i_y, i_x):
    size = 1

    if i_y > 0:
        # up
        if visited_map[i_y - 1][i_x] == -1 and house_map[i_y - 1][i_x] == 1:
            visited_map[i_y - 1][i_x] = 1
            size += DFS(i_y - 1, i_x)
    if i_y < count - 1:
        # down
        if visited_map[i_y + 1][i_x] == -1 and house_map[i_y + 1][i_x] == 1:
            visited_map[i_y + 1][i_x] = 1
            size += DFS(i_y + 1, i_x)
    if i_x > 0:
        # left
        if visited_map[i_y][i_x - 1] == -1 and house_map[i_y][i_x - 1] == 1:
            visited_map[i_y][i_x - 1] = 1
            size += DFS(i_y, i_x - 1)
    if i_x < count - 1:
        # right
        if visited_map[i_y][i_x + 1] == -1 and house_map[i_y][i_x + 1] == 1:
            visited_map[i_y][i_x + 1] = 1
            size += DFS(i_y, i_x + 1)

    return size


for y in range(count):
    for x in range(count):
        if visited_map[y][x] == -1:
            visited_map[y][x] = 1
            if house_map[y][x] == 1:
                house_size.append(DFS(y, x))

house_size.sort()

print(len(house_size))
print("\n".join([str(size) for size in house_size]), end="")
