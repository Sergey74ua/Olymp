arr = []
sPoint = 0
arrX = []
arrY = []
limit = 10**9
arrY.append([0, -1, []])

N, M = map(int, input().split())

for y in range(N):
    arr.append([])
    arrX.clear()
    arrX.append(limit)
    arrX.append(y)
    arrX.append([])

    #Перебор строки
    for x, word in enumerate(input().split()):
        point = int(word)
        arr[y].append(point)
        #Отбор минимальной точки в строке
        if point < arrX[0]:
            arrX.clear()
            arrX.append(point)
            arrX.append(y)
            arrX.append([])
            arrX[2].append(x)
        #Добавляем повторяющиеся минимальные точки
        elif point == arrX[0]:
            arrX[2].append(x)
    
    #Отбор максимальной среди минимальной
    
    if arrX[0] > arrY[0][0]:
        arrY.clear()
        arrY.append(arrX.copy())
    #Добавляем повторяющиеся максимальные точки
    elif arrX[0] == arrY[0][0]:
        arrY.append(arrX)

#Проверка минимальных точек на максимальность в колонке
for arrX in arrY:
    for x in arrX[2]:
        testCountY = 0
        for y in range(N):
            if arrX[0] >= arr[y][x]:
                testCountY += 1
        if testCountY >= N:
            sPoint = arrX[0]
            sPointY = arrX[1]
            sPointX = x
            break

print(sPoint)
if sPoint > 0:
    print(sPointY, sPointX)