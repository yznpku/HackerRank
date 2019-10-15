import calendar

a = list(map(int, input().split()))
b = calendar.weekday(a[2], a[0] , a[1])

c = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(c[b])
