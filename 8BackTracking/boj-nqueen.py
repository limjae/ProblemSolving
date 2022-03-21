def nqueen(n):

    visited = [-1] * n
    cnt = 0
    answers = []

    def is_ok_on(nth_row):
        for row in range(nth_row):
            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                return False
        return True

    def dfs(row):
        if row == n:
            # nonlocal 은 지역변수가 아님을 의미한다.
            nonlocal cnt
            cnt += 1
            print(f"{cnt}번째 답 - visited: {visited}")
            grid = [['.'] * n for _ in range(n)]
            for idx, value in enumerate(visited):
                grid[idx][value] = 'Q'
            result = []
            for row in grid:
                print(row)
                result.append(''.join(row))
            answers.append(result)
            ################
            return

        # visited[row] 의 값을 결정한다.
        # n*n 의 체스판이므로 가능한 열의 범위는 0 ~ n-1 이다.
        for col in range(n):
            # (row, col) 위치에 퀸을 두었다고 가정하고, 규칙을 깨지 않는다면 row+1 행에 다시 퀸을 둔다.
            visited[row] = col
            if is_ok_on(row):
                dfs(row + 1)

    # 0번째 행에 퀸을 둔다.
    dfs(0)
    return answers


assert nqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]