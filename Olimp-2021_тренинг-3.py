N, M = map(int, input().split())
arry = []
strg = []
maxi = []
test = 0

for y in range(N):
    minX = sys.maxsize
    for x in input().split():
        strg.append(int(x))
        if x <= minX:
            minX = x
    arr.append(strg)
    temp.clear()

for x in range(M):
    temp = 0
    for y in range(N):
        if arr[y][x] >= temp:
            temp = arr[y][x]
    maxi.append(temp)

for y in range(N):
    for x in range(M):
        if mini[y] == maxi[x]:
            print(mini[x])
            print(y, x)
            test = 1
            break
    if test == 1:
        break

if test != 1:
    print(0)


#   5 4
#   2 3 2 5
#   1 2 1 3
#   9 8 5 6
#   3 4 3 4
#   2 1 2 3
