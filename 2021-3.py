N, M = map(int, input().split())
arr = []
for y in range(N):
    arr.append(list(map(int, input().split())))

maxY = posX = posY = posMinX = 0
for y in range(N):
    minX = 1000000000
    for x in range(M):
        if arr[y][x] < minX:
            minX = arr[y][x]
            posMinX = x
    if minX > maxY:
        maxY = minX
        posX = posMinX
        posY = y

for y in range(N):
    if maxY < arr[y][posX]:
        maxY = 0
        break

print(maxY)
if maxY > 0:
    print(posY, posX)