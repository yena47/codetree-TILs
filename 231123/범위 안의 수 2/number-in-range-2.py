sum=0
n=0
for i in range(10):
    a=int(input())
    if a>=0 and a<=200:
        sum+=a
        n+=1
mean=sum/n
print(sum, f"{mean:.1f}")