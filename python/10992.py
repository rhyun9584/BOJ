N = int(input())
print(' '*(N-1) + '*')
for i in range(2, N+1):
    if i < N:
        print(' '*(N-i) + '*' + ' '*(2*i-3) + '*')
    else:
        print('*'*(2*i-1))