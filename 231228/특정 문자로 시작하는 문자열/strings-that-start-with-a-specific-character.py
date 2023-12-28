n=int(input())
list=[
    input() for _ in range(n)
]
alpha=input()
count = 0
sum=0

for i in list:
    if i[0]==alpha:
        count += 1
        sum += len(i)
    
print(count, "%.2f"%(sum/count))