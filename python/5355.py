T = int(input())

for _ in range(T):
    arr = list(input().split())

    num = float(arr[0])

    for a in arr[1:]:
        if a == "@":
            num *= 3
        elif a == "%":
            num += 5
        else:
            num -= 7

    print("{:.2f}".format(num))