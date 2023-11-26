arr=[]
for i in range(3):
    a,b=input().split()
    b=int(b)
    if a=='Y':
        if b>=37:
            arr.append("A")
        else:
            arr.append("C")
    else:
        if b>=37:
            arr.append("B")
        else:
            arr.append("D")
count = arr.count("A")
if count>=2:
    print("E")
else: 
    print("N")