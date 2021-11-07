N, M = map(int, input().split())
arr = [list(map(int, input().split())) for y in range(N)]
test = False
arrX = []
minX = 0

for y in range(N):
    temp = min(arr[y])
    if temp > minX:
        minX = temp
        arrX = [y]
    elif temp == minX:
        arrX.append(y)
 
for x, i in enumerate(zip(*arr)):
    tmp = max(i)
    if tmp == minX:
        for y in arrX:
            if arr[y][x] == tmp:
                print(arr[y][x])
                print(y, x)
                test = True
                break
    if test:
        break

if not test:
    print(0)