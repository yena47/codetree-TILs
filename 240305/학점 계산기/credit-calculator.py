n=int(input())
arr=list(map(float,input().split()))

sum_val=0
for i in range(n):
    sum_val+=arr[i]

avg_val=sum_val/n
print(round(avg_val,1))
if avg_val>=4.0:
    print("Perfect")
elif avg_val>=3.0:
    print("Good")
else:
    print("Poor")