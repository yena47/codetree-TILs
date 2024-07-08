n,m=map(int,input().split())
word = list(map(int,input().split()))

cnt=0
for i in range(n):
    if m==word[i]:
        cnt+=1

print(cnt)