K = int(input())

K_bin = bin(K)[2:]
if K == 2 ** (len(K_bin)-1):
    print(K, 0)
else:
    idx = 0
    for i in range(1, len(K_bin)):
        if K_bin[i] == '1':
            idx = i-1

    print(2 ** (len(K_bin)), 2+idx)