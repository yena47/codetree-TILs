n,q=map(int,input().split())
word = list(map(int,input().split()))

for i in range(q):
    Q = list(map(int,input().split()))

    if Q[0]==1:
        a=Q[1]
        print(word[a-1])

    elif Q[0]==2:
        b=Q[1]
        for i in range(n):
            if word[i]==b:
                print(i+1)
                break
        if b not in word:
            print(0)
                
    
    else:
        s=Q[1]
        e=Q[2]
        for i in range(s,e+1):
            print(word[i-1],end=' ')