N = int(input()) # one-base

K = int(input())
apple = []
for i in range(K):
    apple.append(tuple([int(x) for x in input().split()]))

L = int(input())
rotation = {}
for i in range(L):
    list = input().split()
    rotation[int(list[0])] = list[1]

# 0: right, 1: down, 2: left, 3: up
direction = 0
time = 1
snake = [(1, 1)]
while True:
    r = snake[0][0]
    c = snake[0][1]
    if direction == 0:
        head = (r, c+1)
    elif direction == 1:
        head = (r+1 , c)
    elif direction == 2:
        head = (r, c-1)
    elif direction == 3:
        head = (r-1, c)

    if head in snake or head[0] < 1 or head[0] > N or head[1] < 1 or head[1] > N:
        print(time)
        break
        
    if head not in apple:
        snake.pop()
    else:
        apple.remove(head)

    snake = [head] + snake

    d = rotation.get(time)
    if d == 'L':
        direction -= 1
    elif d == 'D':
        direction += 1

    if direction == 4: direction = 0
    elif direction == -1: direction = 3

    time += 1