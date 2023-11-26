a,b,c=map(int,input().split())
yes_or_no=False
for i in range(a,b+1):
    if i%c==0:
        yes_or_no=True

if yes_or_no==True:
    print("YES")
else:
    print("NO")