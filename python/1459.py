X, Y, W, S = map(int, input().split())

minimum = min(X, Y)
maximum = max(X, Y)

if W > S:
    print(minimum*S + ((maximum-minimum)//2*2)*S + ((maximum-minimum)%2)*W)
elif 2*W <= S:
    print((X+Y) * W)
else:
    print(minimum*S + (maximum - minimum)*W)