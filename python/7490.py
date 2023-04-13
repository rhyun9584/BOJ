import re

def dfs(now, max, exp):
    if now > max:
        if eval(re.sub(" ", "", exp)) == 0:
            print(exp)
        
        return
    
    dfs(now+1, max, exp+' '+str(now))
    dfs(now+1, max, exp+'+'+str(now))
    dfs(now+1, max, exp+'-'+str(now))


N = int(input())

for _ in range(N):
    n = int(input())

    dfs(2, n, "1")
    print()