word=list(map(int,input().split()))

max_value=0
min_value=0
for i in word:
    if i==999 or i==-999:
            break
    elif i>max_value:
        max_value=i
    if i<min_value:
        min_value=i
        
print(max_value,min_value)