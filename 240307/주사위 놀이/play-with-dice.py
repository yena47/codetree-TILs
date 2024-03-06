arr=list(map(int,input().split()))

cnt1=0
cnt2=0
cnt3=0
cnt4=0
cnt5=0
cnt6=0

for elem in arr:
    if elem==1:
        cnt1+=1
    elif elem==2:
        cnt2+=1
    elif elem==3:
        cnt3+=1
    elif elem==4:
        cnt4+=1
    elif elem==5:
        cnt5+=1
    else:
        cnt6+=1
    
print(f"1 - {cnt1}")
print(f"2 - {cnt2}")
print(f"3 - {cnt3}")
print(f"4 - {cnt4}")
print(f"5 - {cnt5}")
print(f"6 - {cnt6}")