a,b,c=map(int,input().split())
if a>b:
    if a>c:
        print(a)
    else: 
        print(c)
elif a<b:
    if b>c:
        print(b)
    else:
        print(c)
elif a==b:
    if a>c:
        print(a)
    else: 
        print(c)