def print_rec(a):
    num=1
    for _ in range(a):
        for _ in range(a):
            if num<=9:
                print(num,end=' ')
            else:
                num=1
                print(num,end=' ')
            num+=1
        
        print(end='\n')
          



N=int(input())
print_rec(N)