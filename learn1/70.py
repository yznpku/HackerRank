year=int(input())

def f(year):
    y=str(year)
    if year>=1919:
        if year%400==0 or (year%4==0 and year%100!=0):
            return "12.09."+y
        else: return "13.09."+y

    elif year<=1917:
        if year%4==0:
            return "12.09."+y
        else: return "13.09."+y

    elif year==1918:
        return "28.10.1918"
print(f(year))
