import sys
input = sys.stdin.readline

N, game = input().split()
N = int(N)

player = set()
for _ in range(N):
    player.add(input().rstrip())

answer = len(player)

if game == 'F':
    answer //= 2
if game == 'O':
    answer //= 3

print(answer)