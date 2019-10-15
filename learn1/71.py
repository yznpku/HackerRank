k= list(map(int, input().split()))
k = k[1]
a= list(map(int, input().split()))
b= int(input())

if (sum(a)-a[k])/2==b:
    print("Bon Appetit")
else:
    if int(b-((sum(a)-a[k])/2))==b-((sum(a)-a[k])/2):
        print(int(b-((sum(a)-a[k])/2)))
    else:print(b-((sum(a)-a[k])/2))
