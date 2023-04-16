import sys
input = sys.stdin.readline

N = int(input())

student = []
for _ in range(N):
    student.append(int(input()))
student.sort()

answer = 0
for i in range(N):
    answer += abs((i+1) - student[i])

print(answer)