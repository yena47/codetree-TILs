age1, gender1 = input().split()
age2, gender2 = input().split()
print(1) if (int(age1)>=19 and gender1=="M") or (int(age2)>=19 and gender2=="M") else print(0)