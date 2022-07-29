# https://programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            last = bin(num).rfind('0')
            if last == 0:
                answer.append(num + 2**(len(bin(num)) - 3))
            else:
                answer.append(num + 2**(len(bin(num)) - last - 2))
    return answer