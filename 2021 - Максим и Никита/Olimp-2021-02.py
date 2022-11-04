arr = []
for y in range(3):
    arr.append(list(map(int, input().split())))

S = []
for x in range(3):
    temp = 0
    for y in range(3):
        temp += arr[y][x]
    S.append(temp)
xMin = S.index(min(S))
xMax = S.index(max(S))

for yMin in range(3):
    test = 0
    for yMax in range(3):
        arr[yMin][xMin], arr[yMax][xMax] = arr[yMax][xMax], arr[yMin][xMin]
        if arr[0][xMin]+arr[1][xMin]+arr[2][xMin] == arr[0][xMax]+arr[1][xMax]+arr[2][xMax]:
        # Возможно еще надо проверять сумму строк, а не только колонок
            test = 1
            break
        else:
            arr[yMax][xMax], arr[yMin][xMin] = arr[yMin][xMin], arr[yMax][xMax]
    if test > 0:
        break

for y in range(3):
    print(*arr[y])