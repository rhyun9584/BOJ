N, n1, n2 = [int(x) for x in input().split(" ")]

round = 1
while N > 1:
    n1 = (n1+1) // 2
    n2 = (n2+1) // 2
    
    if n1 == n2:
        print(round)
        break

    round += 1
    N = (N+1) // 2
