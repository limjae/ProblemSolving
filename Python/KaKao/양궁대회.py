def solution(n, info):
    strategies = []
    apeach_score = 0
    answer = [-1]
    last_point = 0
    for index, arrows in enumerate(info):
        score = 10 - index
        if arrows > 0 :
            apeach_score += score

    max_diff = -apeach_score


    def DFS(index, cur_answer, cur_diff, left, last):
        # print(index, cur_answer, cur_diff, left)
        nonlocal max_diff, answer, last_point

        score = 10 - index
        answer_copy = list(cur_answer)

        if index == 10:
            if left > 0:
                answer_copy[10] = left
                last = 10
            if cur_diff > max_diff or (cur_diff == max_diff and last_point <= last):
                print(max_diff, cur_diff, answer_copy)
                max_diff = cur_diff
                answer = list(answer_copy)
                last_point = last
            return 0

        if left > info[index]:
            next_left = left - info[index] - 1
            answer_copy[index] = info[index] + 1
            if info[index] > 0:
                DFS(index + 1, answer_copy, cur_diff + 2 * score, next_left, index)
            else:
                DFS(index + 1, answer_copy, cur_diff + score, next_left, index)

        DFS(index + 1, list(cur_answer), cur_diff, left, last)

    DFS(0,[0 for _ in range(11)], -apeach_score, n, -1)
    print(max_diff, answer)

    return answer if max_diff > 0 else [-1]