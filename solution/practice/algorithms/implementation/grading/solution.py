# Just follow the rules. Straightforward.

for _ in range(int(input())):
  grade = int(input())
  if grade >= 38 and (grade // 5 + 1) * 5 - grade < 3:
    print((grade // 5 + 1) * 5)
  else:
    print(grade)
