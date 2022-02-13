N = int(input())
for i in range(N):
    star = i+1
    space = 2*N - 2*star
    print('*'*star + ' '*space + '*'*star)
for i in range(N-1, 0, -1):
    star = i
    space = 2*N - 2*star
    print('*'*star + ' '*space + '*'*star)