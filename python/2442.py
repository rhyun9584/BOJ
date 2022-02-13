N = int(input())
for i in range(N):
    star = 2*i+1
    space = (2*N-1-star)//2
    print(' '*space+ '*'*star)