arr = []
posX = [0]
maxY = posY = test = 0

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
        posX = [tmpX]
        posY = y
    elif minX == maxY:
        posX.append(tmpX)

for x in posX:
    if all(maxY >= arr[y][x] for y in range(N)):
        print(maxY)
        print(posY, x)
        test = 1

if test == 0:
    print(0)

#Нарушает безопасность