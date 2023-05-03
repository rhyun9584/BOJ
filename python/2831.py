import sys
input = sys.stdin.readline

N = int(input())
men = list(map(int, input().split()))
women = list(map(int, input().split()))

men_plus, men_minus = [], []
for man in men:
    if man > 0:
        men_plus.append(man)
    else:
        men_minus.append(man)
men_plus.sort(reverse=True)
men_minus.sort()

women_plus, women_minus = [], []
for woman in women:
    if woman > 0:
        women_plus.append(woman)
    else:
        women_minus.append(woman)
women_plus.sort(reverse=True)
women_minus.sort()

answer = 0
while men_plus and women_minus:
    if men_plus[-1] >= -women_minus[-1]:
        women_minus.pop()
    else:
        women_minus.pop()
        men_plus.pop()
        answer += 1

while men_minus and women_plus:
    if women_plus[-1] >= -men_minus[-1]:
        men_minus.pop()
    else:
        men_minus.pop()
        women_plus.pop()
        answer += 1

print(answer)
