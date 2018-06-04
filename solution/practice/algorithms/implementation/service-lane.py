n,t = map(int,raw_input().split())
widths = map(int,raw_input().split())
for test in range(t):
	i,j = map(int,raw_input().split())
	print min(widths[i:j+1])
