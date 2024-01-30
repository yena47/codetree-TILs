a,b=map(int,input().split())


def fun_369(n):
    if (n//10)==3 or (n//10)==6 or (n//10)==9 or (n%10)==3 or (n%10)==6 or (n%10)==9:
        return True
    else:
        return False

def is_magic_number(n):
    return n%3==0 or fun_369(n)


cnt=0
for i in range(a, b+1):
    if is_magic_number(i):
        cnt+=1
print(cnt)