print("введите строку ")
s = input()
l = len(s)
m=0
ind=0
count=0
for i in range (l):
    if s[i] !=' ':
        count += 1
    else:
        if count > m:
                m = count
                ind = i - count 
                count = 0
if count > m:
    m = count
    ind = i - count +1
print("результат")
print(s[ind:ind+m])

