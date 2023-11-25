count=0
sum=0
while True:
    age=int(input())
    count+=1
    sum+=age
    if age%20>=10:
        break
mean=(sum-age)/(count-1)
print(f"{mean:.2f}")