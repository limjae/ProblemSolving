from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    if queue1_sum == queue2_sum:
        return 0;

    deque1 = deque(queue1)
    deque2 = deque(queue2)

    while answer < (len(queue1) + len(queue2)) * 2:
        if queue1_sum > queue2_sum:
            pop = deque1.popleft()
            queue1_sum -= pop
            queue2_sum += pop
            deque2.append(pop)
        elif queue1_sum < queue2_sum:
            pop = deque2.popleft()
            queue2_sum -= pop
            queue1_sum += pop
            deque1.append(pop)
        else:
            return answer

        answer += 1

    if queue1_sum == queue2_sum:
        return answer
    else:
        return -1
