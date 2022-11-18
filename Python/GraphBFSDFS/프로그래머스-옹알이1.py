# https://school.programmers.co.kr/learn/courses/30/lessons/120956
def solution(babbling):
    answer = 0
    speak_available = ["aya", "ye", "woo", "ma"]
    already_speak = [False for _ in range(4)]
    word_available = set()

    def DFS(word):
        for nxt_index, nxt in enumerate(speak_available):
            if already_speak[nxt_index] == False:
                already_speak[nxt_index] = True
                word_available.add(word + nxt)
                DFS(word + nxt)
                already_speak[nxt_index] = False

    DFS('')

    for bab in babbling:
        if bab in word_available:
            answer += 1
    return answer
