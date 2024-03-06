arr=list(map(int,input().split()))
count_arr=[0]*7

# 카운팅 배열을 통해 각각의 빈도 저장. 인덱스값 고려하여 일부러 7칸 배열 만든 것
for elem in arr:
    count_arr[elem]+=1

for i in range(1,7):
    print(f"{i} - {count_arr[i]}")