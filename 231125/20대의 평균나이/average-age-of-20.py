count=0
sum=0
while True:
    age=int(input())
    count+=1
    sum+=age
    if age%20>=10:
        sum-=age
        count-=1
        break
mean=sum/count
print(f"{mean:.2f}")