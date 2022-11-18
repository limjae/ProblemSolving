def solution(board):
    check_range = [
        [0, 1],

        [1, 1],
        [1, 0],
        [1, -1],

        [0, -1],

        [-1, -1],
        [-1, 0],
        [-1, 1]
    ]
    answer = 0
    n = len(board)

    for x in range(n):
        for y in range(n):
            chk = True
            if board[y][x] == 1:
                continue

            for d in check_range:
                dx, dy = d
                if -1 < x + dx < n and -1 < y + dy < n and board[y + dy][x + dx] == 1:
                    chk = False

            if chk:
                answer += 1

    return answer
