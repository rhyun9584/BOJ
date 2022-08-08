import sys
input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

count = [0, 0, 0]
def dfs(x, y, n):
    global count

    num = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3, y+l*n//3, n//3)
                return
    
    count[num+1] += 1

dfs(0, 0, N)
for i in range(3):
    print(count[i])