arr=list(map(int,input().split()))
sum_odd=arr[0]+arr[2]+arr[4]+arr[6]+arr[8]
sum_even=arr[1]+arr[3]+arr[5]+arr[7]+arr[9]

if sum_even>=sum_even:
    print(sum_even-sum_odd)
else:
    print(sum_odd-sum_even)