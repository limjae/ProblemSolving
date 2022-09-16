# 누적합 연산 문제...
def solution(board, skill):
    answer = 0
    acc_board = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for cur_skill in skill:
        s_type, r1, c1, r2, c2, degree = cur_skill

        if s_type == 1:
            degree = -degree

        acc_board[r1][c1] += degree
        acc_board[r1][c2 + 1] -= degree
        acc_board[r2 + 1][c1] -= degree
        acc_board[r2 + 1][c2 + 1] += degree

    for x in range(len(board[0])):
        for y in range(len(board)):
            acc_board[y][x + 1] += acc_board[y][x]

    for y in range(len(board)):
        for x in range(len(board[0])):
            acc_board[y + 1][x] += acc_board[y][x]

    # print(board)
    # print(acc_board)

    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col + acc_board[y][x] > 0:
                answer += 1
    return answer
