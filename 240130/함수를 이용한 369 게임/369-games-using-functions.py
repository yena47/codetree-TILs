a,b=map(int,input().split())


def contains_369(n):
    while n>0:
        if n%10==3 or n%10==6 or n%10==9:
            return True
        n//=10
    return False

def is_magic_number(n):
    return n%3==0 or contains_369(n)


cnt=0
for i in range(a, b+1):
    if is_magic_number(i):
        cnt+=1
print(cnt)