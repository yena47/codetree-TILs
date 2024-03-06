n=int(input())

cnt_5times=0

for i in range(1,100):
    print(n*i,end=' ')
    
    if (n*i)%5==0:
        cnt_5times+=1
        
    if cnt_5times==2:
        break