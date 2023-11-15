a1,a2=map(int,input().split())
arr=[0,a1,a2]

for i in range(3,11):
    arr.append((arr[-1]+arr[-2])%10)

for i in range(1,11):
    print(arr[i],end=' ')