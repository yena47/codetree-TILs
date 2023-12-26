a=input()
arr=['apple', 'banana', 'grape', 'blueberry', 'orange']
count=0
for i in arr:
    if (i[2] == a) or (i[3] == a):
        count += 1
        print(i, end='\n')
print(count)