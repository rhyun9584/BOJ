A, B, C = map(int, input().split())
D = int(input())

D_s = D % 60
D_m = D // 60 % 60
D_h = D // (60**2)

C += D_s
while C >= 60:
    C -= 60
    B += 1

B += D_m
while B >= 60:
    B -= 60
    A += 1

A += D_h
while A >= 24:
    A -= 24

print(A, B, C)