n=int(input())
cnt_pass=0

for i in range(n):
    score= list(map(int,input().split()))
    avg_socre=sum(score)/len(score)

    if avg_socre>=60:
        print("pass")
        cnt_pass+=1
    else:
        print("fail")

print(cnt_pass)