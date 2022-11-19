# https://school.programmers.co.kr/learn/courses/30/lessons/120883

def solution(id_pw, db):
    db_dict = {}
    for data in db:
        db_dict[data[0]] = data[1]

    if id_pw[0] not in db_dict:
        return "fail"
    if id_pw[1] != db_dict[id_pw[0]]:
        return "wrong pw"
    return "login"
