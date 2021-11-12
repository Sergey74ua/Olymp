arr = []
pos = [[0, 0]]
maxY = tmpX = test = 0

N, M = map(int, input().split())
for y in range(N):
    arr.append(list(map(int, input().split())))

for y in range(N):
    minX = 1000000000
    for x in range(M):
        if arr[y][x] < minX:
            minX = arr[y][x]
            tmpX = x
    if minX > maxY:
        maxY = minX
        pos.clear()
        pos.append([y, tmpX])
    elif minX == maxY:
        pos.append([y, tmpX])

for i in pos:
    for y in range(N):
        if maxY < arr[y][i[1]]:
            test = 0
            break
        else:
            test += 1
    if test >= N:
        print(maxY)
        print(i[0], i[1])
        maxY = False
        break

if maxY:
    print(0)