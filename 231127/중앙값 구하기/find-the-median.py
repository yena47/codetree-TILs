a,b,c=map(int,input().split())
if a>b:
    if a>c:
        if b>c:
            print(b)
        else:
            print(c)
    else: 
        print(a)
elif a<b:
    if b>c:
        if a>c:
            print(a)
        else: 
            print(c)
    else: 
        print(b)
else:
    if a>c:
        print(a)
    else:
        print(c)