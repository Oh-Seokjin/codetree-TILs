class Student:
    def __init__(self, h, w, n):
        self.h, self.w, self.n = h, w, n

n = int(input())

inputs = [map(int, input().split()) for _ in range(n)]
students = [Student(h, w, n+1) for n, (h, w) in enumerate(inputs)]

students.sort(key = lambda x: (-x.h, x.w), reverse=True)

for student in students:
    print(student.h, student.w, student.n)