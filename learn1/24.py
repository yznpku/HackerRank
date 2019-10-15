def grade(grades):
    round = []
    for i in grades:
        if i<=37:
            round.append(i)
        else:
            k=0
            for j in range(3):
                if (i+j)%5==0:
                    k+=1
                    round.append(i+j)
            if k==0:
                round.append(i)
    return round


n = int(input())

grades = []

for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)

result = grade(grades)
print(result)
