def add(a,b,c):
    if a<b:
        if a<c:
            min=a
        else:
            min=c
    else:
        if b<c:
            min=b
        else:
            min=c
    return min
    

a,b,c=map(int,input().split())
print(add(a,b,c))