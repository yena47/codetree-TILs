A1,A2=map(int,input().split())
arr=[A1,A2]
cnt=1

# 배열 생성
while cnt<9:
    cnt+=1
    arr.append(arr[cnt-1]+2*arr[cnt-2])

# 배열 출력
for elem in arr:
    print(elem, end=' ')