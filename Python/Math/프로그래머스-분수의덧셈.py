# https://school.programmers.co.kr/learn/courses/30/lessons/120808
import math


def solution(denum1, num1, denum2, num2):
    lcm = (num1 * num2) // math.gcd(num1, num2)
    mult1 = lcm // num1
    mult2 = lcm // num2

    denum = (denum1 * mult1 + denum2 * mult2) // math.gcd((denum1 * mult1 + denum2 * mult2), lcm)
    num = lcm // math.gcd((denum1 * mult1 + denum2 * mult2), lcm)

    return [denum, num]