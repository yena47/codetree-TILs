a,b=map(int,input().split())


def fun_369(n):
    for i in str(n):
        if int(i)==3 or int(i)==6 or int(i)==9:
            return True

def is_magic_number(n):
    return n%3==0 or fun_369(n)


cnt=0
for i in range(a, b+1):
    if is_magic_number(i):
        cnt+=1
print(cnt)