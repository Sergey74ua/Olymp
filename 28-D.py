N = int(input())
prev = 0
temp = 0
maxi = 0
for i in map(int, input().split()):
    if i > prev:
        temp = 1
    else:
        temp += 1
    if temp >= maxi:
        maxi = temp
    prev = i
print(maxi)