# When we read a row, we add the number in one diagonal and subtract
# the one in the other. Pretty straightforward right?

N = int(input())
sum = 0
for i in range(N):
  row = list(map(int, input().split()))
  sum += row[i] - row[N - i - 1]
print(abs(sum))
