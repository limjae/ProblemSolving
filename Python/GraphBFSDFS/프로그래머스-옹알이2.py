# https://school.programmers.co.kr/learn/courses/30/lessons/133499
def solution(babbling):
    answer = 0
    speak_available = ["aya", "ye", "woo", "ma"]

    word_available = set()

    def DFS(word, prev):
        for nxt_index, nxt in enumerate(speak_available):
            if nxt != prev and len(word) < 30:
                word_available.add(word + nxt)
                DFS(word + nxt, nxt)

    DFS('', '')

    for bab in babbling:
        if bab in word_available:
            answer += 1
    return answer
