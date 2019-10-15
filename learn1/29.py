n, inputs = [int(n) for n in input().split()]
arr = list(map(int, input().split()))

a = arr[inputs:]+arr[:inputs]
print(' '.join(str(i) for i in a))
