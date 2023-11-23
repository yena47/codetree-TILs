a,b=map(int,input().split())
sum=0
n=0
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        sum += i
        n+=1

mean = sum/n
print(sum, f"{mean:.1f}")