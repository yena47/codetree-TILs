arr=list(map(int,input().split()))
cnt_arr=[0]*10

# 십의자리수가 3이면 cnt_arr[3]에 1 카운팅하기
for elem in arr:
    if elem != 0:
        cnt_arr[elem//10]+=1
    else:
        break

for i in range(1,10):
    print(f"{i} - {cnt_arr[i]}")