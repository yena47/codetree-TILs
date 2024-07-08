n,q=map(int,input().split())
word = list(map(int,input().split()))

for i in range(q):
    question = list(map(int,input().split()))

    if question[0]==1:
        print(question[1])

    elif question[0]==2:
        b=question[1]
        for i in range(n):
            if word[i]==b:
                print(i+1)
                break
            elif b not in word:
                print(0)
                
    
    else:
        s=question[1]
        e=question[2]
        for i in range(s,e+1):
            print(word[i-1],end=' ')