from collections import deque

# ~ 9999 까지의 수 소수 판별
MAX = 10000
is_prime = [True for _ in range(MAX)]
for i in range(2, MAX):
    if is_prime[i] == True:
        j = 2
        while i*j < MAX:
            is_prime[i*j] = False
            j += 1

T = int(input())
for _ in range(T):
    s, e = input().split()

    result = -1

    queue = deque([s])
    visited = [-1] * (MAX-1000)
    visited[int(s)-1000] = 0
    while queue:
        n = queue.popleft()
        if n == e:
            result = visited[int(n)-1000]
            break

        for i in range(4):
            for j in range(10):
                if s[i] == str(j) or (i == 0 and j == 0):
                    continue

                new_s = f'{n[:i]}{j}{n[i+1:]}'
                if is_prime[int(new_s)] and visited[int(new_s)-1000] == -1:
                    visited[int(new_s)-1000] = visited[int(n)-1000]+1
                    queue.append(new_s)


    if result >= 0:
        print(result)
    else:
        print("Impossible")