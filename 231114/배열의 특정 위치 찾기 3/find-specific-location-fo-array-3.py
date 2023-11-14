arr = list(map(int,input().split()))
n = len(arr)

sum=0
for i in range(n):
    sum+=arr[i]
    if arr[i]==0:
        break

print(sum)