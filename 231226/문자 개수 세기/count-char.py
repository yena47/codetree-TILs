string=input()
alphabet=input()
count = 0
for i in string:
    if i == alphabet:
        count += 1
print(count)