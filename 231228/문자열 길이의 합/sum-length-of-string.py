n=int(input())
arr=[]
for i in range(n):
    string=input()
    arr.append(string)

length=0
count=0
for i in arr:
    length += len(i)
    if i[0] == 'a':
        count += 1
print(length,count)