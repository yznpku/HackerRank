import sys
import math

def solve(grades):
    # Complete this function
    toReturn = ""
    for grade in grades:
        newGrade = 0
        c = grade % 5
        if(grade >= 38 and 5-c < 3 and c != 0):
            newGrade = grade + 5- c
            if (newGrade > 100):
                newGrade = 100
            print(str(newGrade))
        else:
            newGrade = grade
            print(str(newGrade))


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
