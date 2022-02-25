import sys

N, K = [int(x) for x in sys.stdin.readline().split()]
list = [x for x in range(1, N+1)]
idx = K-1
l = N-1
print(f"<{list.pop(idx)}", end="")
while l > 0:
    print(", ", end="")

    idx = (idx + K - 1) % l
    print(f"{list.pop(idx)}", end="")
    
    l -= 1

print(">")