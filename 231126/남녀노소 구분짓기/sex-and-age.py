sex, age=map(int,input().split())
if sex==0:
    if age>=19:
        print("MAN")
    else: 
        print("BOY")
if sex==1:
    if age>=19:
        print("WOMAN")
    else: 
        print("GIRL")