from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    child_finder = defaultdict(lambda: -1)
    index_finder = defaultdict(lambda: -1)
    referal_dict = defaultdict(str)

    for i, parent in enumerate(referral):
        child = enroll[i]
        child_finder[child] = i
        referal_dict[child] = parent

    for i, child in enumerate(enroll):
        parent = referal_dict[child]
        parent_index = child_finder[parent]
        index_finder[i] = parent_index
    print(index_finder)
    for i, who in enumerate(seller):
        profit = amount[i] * 100

        index = child_finder[who]
        answer[index] += profit

        while index_finder[index] > -1 and profit > 9:
            profit = profit // 10
            answer[index] -= profit
            index = index_finder[index]
            answer[index] += profit

        profit = profit // 10
        answer[index] -= profit

    return answer
