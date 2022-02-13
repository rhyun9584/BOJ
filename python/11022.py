T = int(input())
for i in range(T):
    A, B = [int(x) for x in input().split()]
    print(f"Case #{i+1}: {A} + {B} = {A+B}")