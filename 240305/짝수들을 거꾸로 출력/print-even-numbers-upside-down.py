n=int(input())
arr=list(map(int,input().split()))

list_even=[]
cnt_even=0

for elem in arr:
    if elem%2==0:
        list_even.append(elem)
        cnt_even+=1

for i in range(cnt_even,0,-1):
    print(list_even[i-1],end=' ')