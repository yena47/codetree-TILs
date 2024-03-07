arr=list(map(int,input().split()))
cnt_arr=[0]*11

for elem in arr:
    if elem != 0:
        cnt_arr[elem//10]+=1
    else:
        break

for i in range(10,0,-1):
    print(f"{i*10} - {cnt_arr[i]}")