n=int(input())
arr=[]
arr.append(1)
arr.append(n)
print(arr[0],arr[1],end=' ')

for i in range(1,100):
    value=arr[i]+arr[i-1]
    arr.append(value)
    print(arr[i+1], end=' ')
    if arr[i+1]>100:
        break