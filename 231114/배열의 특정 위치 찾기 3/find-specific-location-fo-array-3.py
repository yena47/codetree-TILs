arr = list(map(int,input().split()))
n = len(arr)

for i in range(n):
    if arr[i]==0:
        sum=arr[i-1]+arr[i-2]+arr[i-3]
        break

print(sum)