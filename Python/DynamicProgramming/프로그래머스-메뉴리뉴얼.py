# https://programmers.co.kr/learn/courses/30/lessons/72411

import collections

def solution(orders, course):
    answer = []
    order_set = [set(order) for order in orders]
    available_set = collections.defaultdict(list)

    total_type = set()
    for order in orders:
        for c in order:
            total_type.add(c)

    for c in total_type:
        subset_count = 0
        for o in order_set:
            if c in o:
                subset_count += 1
        if subset_count > 1:
            available_set[1].append(c)

    for nums in range(2, max(course) + 1):
        tmp_comb_set = list()
        for set1 in available_set[nums - 1]:
            for set2 in available_set[1]:
                tmp = set(set1).union(set(set2))
                if len(tmp) == nums and tmp not in tmp_comb_set:
                    tmp_comb_set.append(set(set1).union(set(set2)))

        max_count = 0
        tmp_comb_count = collections.defaultdict(list)
        for comb in tmp_comb_set:
            subset_count = 0
            for o in order_set:
                if comb.issubset(o) == True:
                    subset_count += 1
            if subset_count > 1:
                available_set[nums].append(comb)
                tmp_comb_count[subset_count].append(''.join(sorted(comb)))
                max_count = max(max_count, subset_count)

        if nums in course:
            answer += tmp_comb_count[max_count]

    return sorted(answer)


