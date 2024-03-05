arr=list(map(int,input().split()))
cnt_even=0
sum_even=0

for elem in arr:
    if elem==0:
        break
    elif elem%2==0:
        cnt_even+=1
        sum_even+=elem

print(cnt_even,sum_even)