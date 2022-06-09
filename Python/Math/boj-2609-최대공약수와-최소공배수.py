import sys
a, b = list(map(int, sys.stdin.readline().split()))

if a < b:
    a,b = b,a

gcd_a, gcd_b = a, b
while gcd_b != 0:
    gcd_a, gcd_b = gcd_b, gcd_a % gcd_b

print(gcd_a)
print(a*b//gcd_a)