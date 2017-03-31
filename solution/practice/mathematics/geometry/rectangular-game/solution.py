# Since all rectangles will cover (1, 1), X should always equal N.
# Therefore we just have to find the area that all rectangles intersect.

X, Y = [], []
for i in range(int(input())):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)
print(min(X) * min(Y))
