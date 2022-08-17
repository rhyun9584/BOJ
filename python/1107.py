N = int(input())
M = int(input())
wrong = set()
if M > 0:
    wrong.update(input().split())

result = abs(N-100)
for n in range(1000001):
    can_make = True
    for ch in str(n):
        if ch in wrong:
            can_make = False
            break
    
    if can_make:
        result = min(result, len(str(n))+abs(n-N))

print(result)