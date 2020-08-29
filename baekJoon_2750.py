size = int(input())

if size <= 1000:
    if(size >= 1):
        a = list()

i = 0
while i < size:
    num = int(input())
    a.append(num)
    i = i + 1

a.sort()

j = 0
for j in a:
    print(j)