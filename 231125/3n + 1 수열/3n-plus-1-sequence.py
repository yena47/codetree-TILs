count=0
n=int(input())
while True:
    if n==1:
        break
    count+=1
    if n%2==0:
        n/=2
    else:
        n=n*3+1
print(count)