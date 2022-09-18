import sys

N = int(input())

def dfs(string, n):
    for i in range(n//2):
        j = i+1
        if string[n-2*j:n-j] == string[n-j:n]:
            return 
            
    if n == N:
        print(string)
        sys.exit()

    dfs(string+"1", n+1)
    dfs(string+"2", n+1)
    dfs(string+"3", n+1)

dfs("1", 1)