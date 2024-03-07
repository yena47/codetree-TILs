cnt_arr=[0]*4

for i in range(3):
    cold,temp=input().split()
    temp=int(temp)

    if cold=="Y" and temp>=37:
        cnt_arr[0]+=1
    elif cold=="N" and temp>=37:
        cnt_arr[1]+=1
    elif cold=="Y" and temp<37:
        cnt_arr[2]+=1
    else:
        cnt_arr[3]+=1

for elem in cnt_arr:
    print(elem,end=' ')
if cnt_arr[0]>=2:
    print("E")