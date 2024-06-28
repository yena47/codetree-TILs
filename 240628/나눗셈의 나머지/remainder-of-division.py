a,b=map(int,input().split())
count_arr=[0]*b

# 개수 세기
while True:
    a=a//b
    count_arr[a%b]+=1
    if a<=1:
        break

# 출력하기
sum=0
for elem in count_arr:
    sum+=elem**2
print(sum)