def print_rec(a,b):
    for i in range(a):
        print("1"*b)


n,m=tuple(map(int,input().split()))
print_rec(n,m)