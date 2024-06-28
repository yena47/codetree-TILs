n=int(input())
arr=list(map(int,input().split()))

# 개수 세기
count_arr=[0]*10
 
for elem in arr:
    count_arr[elem]+=1

# 개수 출력
for i in range(1,10):
    print(count_arr[i])