n=int(input())

for i in range(n-1,-1,-1):
    for j in range(i+1):
        print("*", end=' ')
    print()
    
for i in range(1,n):
    for j in range(i+1):
        print("*", end=' ')
    print()