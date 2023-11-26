cm,kg=map(int,input().split())
m=cm/100
bmi=kg//(m**2)
print(int(bmi))
if bmi>=25:
    print("Obesity")