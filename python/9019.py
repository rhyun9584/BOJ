from collections import deque


T = int(input())

for _ in range(T):
    s, e = map(int, input().split())

    queue = deque([(s, '')])
    
    visited = [0] * 10000
    visited[s] = 1

    result = 0
    while queue:
        n, op_list = queue.popleft()
        if n == e:
            print(op_list)
            break

        new = (n*2)%10000
        if visited[new] == 0:
            visited[new] = 1
            queue.append((new, op_list+'D'))
        
        if n == 0: new = 9999
        else: new = n-1
        if visited[new] == 0:
            visited[new] = 1
            queue.append((new, op_list+'S'))
        
        new = (n%1000)*10 + n//1000
        if visited[new] == 0:
            visited[new] = 1
            queue.append((new, op_list+'L'))
        
        new = (n%10)*1000 + n//10
        if visited[new] == 0:
            visited[new] = 1
            queue.append((new, op_list+'R'))
        