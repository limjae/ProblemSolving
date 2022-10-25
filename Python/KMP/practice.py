def fail_function(pattern):
    print("pattern: " + pattern)
    rollback_list = [0 for _ in pattern]

    # index 0은 항상 0임
    cur_point = 1
    rollback_len = 0
    while cur_point < len(pattern):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pattern[cur_point] == pattern[rollback_len]:
            rollback_len += 1
            rollback_list[cur_point] = rollback_len
            cur_point += 1
        else:
            # 일치하지 않는 경우
            if rollback_len != 0:
                print("pattern: " + pattern[:cur_point] + " miss, try at : " + pattern[:rollback_list[rollback_len - 1]])
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                rollback_len = rollback_list[rollback_len - 1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                rollback_list[cur_point] = 0
                cur_point += 1

    return rollback_list


def KMP(pattern, txt):
    rollback_list = fail_function(pattern)

    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < len(txt):
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pattern[j] == txt[i]:
            i += 1
            j += 1
        # Pattern을 찾지 못한 경우
        elif pattern[j] != txt[i]:
            # j!=0인 경우는 짧은 lps에 대해 재검사
            if j != 0:
                j = rollback_list[j - 1]
            # j==0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1

        # Pattern을 찾은 경우
        if j == len(pattern):
            print("Found pattern at index " + str(i - j))
            # 이전 인덱스의 lps값을 참조하여 계속 검색
            j = rollback_list[j - 1]


print(fail_function("ABVAB"))
# AB 0
# ABV 0
# ABVA 1 "A"
# ABVAB 2 "AB"

print(fail_function("ABABC"))
# AB 0
# ABA 1 "A"
# ABAB 2 "AB"
# ABABC 0

print(fail_function("ABABABABCABABABABABAB"))

print(fail_function("ABABB"))
# AB 0
# ABA 1 "A"
# ABAB 2 "AB"
# ABABB 0


print(fail_function("AAAAAAAE"))

KMP("AAAAAAAE", "AAAAAAAAAAAAAAAEAAAAAAAAAAAAE")
