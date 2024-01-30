def is_magic_val(n):
    sum=0
    for i in n:
        sum+=int(i)
    return int(n)%2==0 and sum%5==0

n=input()
if is_magic_val(n):
    print("Yes")
else:
    print("No")