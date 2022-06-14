
# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    word_arr = [word.lower().capitalize() for word in s.split(" ")]
    return " ".join(word_arr)