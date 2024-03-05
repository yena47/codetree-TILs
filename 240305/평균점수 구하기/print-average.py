arr=list(map(float,input().split()))
sum=0
for i in arr:
    sum+=i
avg=sum/len(arr)
print(round(avg,1))