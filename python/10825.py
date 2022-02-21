import sys

student = sys.stdin.readlines()[1:]
student.sort(key=lambda x: x.split()[0])
student.sort(key=lambda x: int(x.split()[3]), reverse=True)
student.sort(key=lambda x: int(x.split()[2]))
student.sort(key=lambda x: int(x.split()[1]), reverse=True)

for i in range(len(student)):
    print(student[i].split()[0])