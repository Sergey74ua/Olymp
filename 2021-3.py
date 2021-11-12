N, M = map(int, input().split())
arr = []
maxY = 0
pos = 0

for y in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    minX = 1000000000
    for x in range(M):
        if row[x] < minX:
            minX = row[x]
    if minX > maxY:
        maxY = minX
        pos = y

for x in range(M):
    if maxY == arr[pos][x]:
        for y in range(N):
            if maxY < arr[y][x]:
                break
            if y == N - 1:
                print(maxY)
                print(pos, x)
                maxY = 0
                break

if maxY:
    print(0)