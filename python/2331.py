A, P = map(int, input().split())

D = [A]
now = D[0]
while True:
    next = sum([int(x) ** P for x in str(now)])

    # 새로 계산한 수가 만약 이미 순열에 존재한다면 반복 시작
    if next in D:
        idx = D.index(next)
        print(idx)
        break

    D.append(next)
    now = next