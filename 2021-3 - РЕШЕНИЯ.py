# 19 тестов 50 баллов *************************************************

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

# 19 тестов 50 баллов *************************************************

a =[list(map(int, input().split())) for _ in range(n)]
for i, row in enumerate(a):
    min_in_row = min(row)
    min_idx_in_col = row.index(min_in_row)
    if all(min_in_row >= a[j][min_idx_in_col] for j in range(n)):
        print(f'{min_in_row}\n{i} {min_idx_in_col}')
        break
else:
    print(0)

# 30 тестов 100 баллов ************************************************

def foo(n, m, a):
    for i, row in enumerate(a):
        min_in_row = min(row)
        for min_idx_in_col in [idx for idx in range(m) if row[idx] == min_in_row]:
            if all(min_in_row >= a[j][min_idx_in_col] for j in range(n)):
                print(min_in_row)
                print(i, min_idx_in_col)
                return
    print(0)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
foo(n, m, a)

# 30 тестов 100 баллов ************************************************

n, m = map(int, input().split())
im = []
a =[list(map(int, input().split())) for i in range(n)]
flag = False
res = min_tmp = 0
for i in range(n):
    tmin = min(a[i])
    if tmin > min_tmp:
        min_tmp = tmin
        im = [i]
    elif tmin == min_tmp:
        im.append(i)
for j, v in enumerate(zip(*a)):
    tmp = max(v)
    if tmp == min_tmp:
        for i in im:
            if a[i][j] == tmp:
                res = f'{a[i][j]}\n{i} {j}'
                flag = True
                break
    if flag:
        break
print(res)

# 30 тестов 100 баллов ************************************************

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

# 30 тестов 100 баллов ************************************************

N, M = map(int, input().split())
test = False
arr = []
arrX = []
minX = 0

for y in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
    temp = min(line)
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