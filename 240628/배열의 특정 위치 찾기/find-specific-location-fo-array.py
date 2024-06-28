arr=list(map(int,input().split()))

filtered_arr1=arr[1::2]
sum_value=sum(filtered_arr1)

n=len(arr)

sum=0
count=0
for i in range(2,n,3):
    sum+=arr[i]
    count+=1
average=round(sum/count,1)

print(sum_value, average)