import sys

crane_length = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split()))
cranes.sort()

load_length = int(sys.stdin.readline())
loads = list(map(int, sys.stdin.readline().split()))
loads.sort()

minutes = 0
if max(loads) > max(cranes):
    print(-1)
else:
    while loads:
        minutes += 1
        for crane in cranes:
            for load_index in range(len(loads)-1, -1, -1):
                if crane >= loads[load_index]:
                    loads.remove(loads[load_index])
                    break
    print(minutes)

