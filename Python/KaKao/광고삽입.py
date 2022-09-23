def solution(play_time, adv_time, logs):

    answer = 0
    max_people = 0
    max_total = 0

    log_list = [0 for _ in range(strtotime(play_time)+1)]

    for log in logs:
        start, end = log.split("-")
        log_list[strtotime(start)] += 1
        log_list[strtotime(end)] -= 1

    for i in range(strtotime(play_time)):
        log_list[i+1] += log_list[i]

    cur_total = 0
    j = 0
    for i in range(strtotime(play_time)):
        if i > 0:
            cur_total -= log_list[i-1]

        while j - i < strtotime(adv_time) and j < strtotime(play_time):
            cur_total += log_list[j]
            j += 1

        if cur_total > max_total:
            answer = i
            max_total = cur_total


    return timetostr(answer)

def strtotime(stime):
    h, m, s = stime.split(":")
    time = 3600*int(h) + 60*int(m) + int(s)
    return time

def timetostr(time):
    h = time // 3600
    m = (time % 3600) // 60
    s = time % 60
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


