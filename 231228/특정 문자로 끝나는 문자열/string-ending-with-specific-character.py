list=[
    input() for _ in range(10)
]
alpha=input()
count=0
for i in list:
    if i[-1]==alpha:
        print(i)
        count+=1
if count==0:
    print("None")