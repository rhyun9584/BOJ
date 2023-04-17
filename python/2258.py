N, M = map(int, input().split())

meat = []
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    
    total += a
    meat.append((a, b))

if total < M:
    print(-1)
else:
    meat.sort(key=lambda x: (x[1], -x[0]))

    cnt = 1
    total_size, before_cost = meat[0]

    result = [meat[0]]
    for i in range(1, N):
        size, cost = meat[i]

        if before_cost == cost:
            cnt += 1
        else:
            before_cost = cost
            cnt = 1
        
        total_size += size
        result.append((total_size, before_cost*cnt))

        if total_size >= M and cnt == 1:
            break

    result.sort(key=lambda x: (x[1], -x[0]))

    for size, cost in result:
        if size >= M:
            print(cost)
            break
